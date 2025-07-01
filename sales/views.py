from django.shortcuts import render
from django.views.generic import ListView, DetailView
from sales.models import Sale

class SalesListView(ListView):
	model = Sale


class SalesDetailView(DetailView):
	model = Sale