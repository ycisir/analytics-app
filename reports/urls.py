from django.urls import path
from reports import views

app_name = 'reports'

urlpatterns = [
    path('', views.ReportListView.as_view(), name='list'),
    path('save/', views.create_report_view, name='create_report'),
    path('upload/', views.csv_upload_view, name='upload'),
    path('from_file/', views.UploadTemplateView.as_view(), name='from_file'),
    path('<pk>/', views.ReportDetailView.as_view(), name='detail'),
    path('<pk>/pdf/', views.render_pdf_view, name='pdf'),
]