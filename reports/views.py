from django.shortcuts import render, get_object_or_404
from core.models import Profile
from django.http import JsonResponse, HttpResponse
from reports.utils import get_report_image
from reports.models import Report
from reports.forms import ReportForm
from django.views.generic import ListView, DetailView, TemplateView

from django.conf import settings
from django.contrib.staticfiles import finders
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

from sales.models import Position, CSV, Sale
import csv
from django.utils.dateparse import parse_date


class ReportListView(ListView):
    model = Report

class ReportDetailView(DetailView):
    model = Report

class UploadTemplateView(TemplateView):
    template_name = 'reports/from_file.html'

def csv_upload_view(request):
    print('file is being send...')
    
    if request.method == 'POST':
        csv_file = request.FILES.get('file')
        obj = CSV.objects.create(file_name=csv_file)

        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)
            reader.__next__()
            for row in reader:
                print(row, type(row))
                transaction_id = row[1]
                product = row[2]
                quantity = int(row[3])
                customer = row[4]
                date = parse_date(row[5])

    return HttpResponse()

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def create_report_view(request):
    form = ReportForm(request.POST or None)

    if is_ajax(request=request):
        # name = request.POST.get('name')
        # remarks = request.POST.get('remarks')

        image = request.POST.get('image')
        img = get_report_image(image)
        author = Profile.objects.get(user=request.user)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.image = img
            instance.author = author
            instance.save()

        # Report.objects.create(name=name, remarks=remarks, image=img, author=author)
        return JsonResponse({'msg': 'send'})
    
    return JsonResponse({})


def render_pdf_view(request, pk):
    template_path = 'reports/pdf.html'
    obj = get_object_or_404(Report, pk=pk)
    context = {'obj': obj}

    # Create a Django response object, and set content type to PDF
    response = HttpResponse(content_type='application/pdf')

    # if download
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    # if display
    response['Content-Disposition'] = 'filename="report.pdf"'

    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html,
       dest=response,
    )

    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')

    return response
