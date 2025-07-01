from django.urls import path
from sales import views

urlpatterns = [
    path('', views.SalesListView.as_view(), name='list'),
    path('<int:pk>', views.SalesDetailView.as_view(), name='detail'),
]