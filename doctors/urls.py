from . import views
from django.urls import path
from .views import doctors_list

urlpatterns = [
    path('', views.doctors_list, name='doctors_list')
]