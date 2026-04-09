from django.urls import path
from . import views                    # <-- ADD THIS IMPORT

urlpatterns = [
    path('', views.patient_list),      # <-- prefix with views.
    path('<int:pk>/edit', views.patient_edit),
    path('<int:pk>/delete', views.patient_delete),
    path('create/', views.patient_create)
       # <-- prefix with views.
]