from django import forms
from reports.models import Report

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('name', 'remarks')
    
    def __init__(self, *args, **kwargs):
        super(ReportForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['remarks'].widget.attrs.update({'class': 'form-control'})