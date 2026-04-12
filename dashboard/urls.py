from django.urls import path
from . import views
    
urlpatterns = [
    path('', views.dashboard_home, name='dashboard'),
    path('ai/', views.dashboard_hms_ai, name='dashboard_hms_ai')
]
