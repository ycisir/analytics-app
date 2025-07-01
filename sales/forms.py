from django import forms

CHART_CHOICES = (
    ('#1', 'Bar chart'),
    ('#2', 'Pie chart'),
    ('#3', 'Line chart'),
)

RESULT_CHOICES = (
    ('#1', 'Transaction'),
    ('#2', 'Sales date'),
)

class SalesSearchForm(forms.Form):
    date_from = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control'
        })
    )
    date_to = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control'
        })
    )
    chart_type = forms.ChoiceField(
        choices=CHART_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
    results_by = forms.ChoiceField(
        choices=RESULT_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )