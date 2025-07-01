from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('my_profile', views.my_profile_view, name='my_profile'),
]