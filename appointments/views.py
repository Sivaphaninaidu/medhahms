from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Appointment
from django.utils.decorators import method_decorator
from django import views
# Create your views here.


# @login_required
# def appointment_list(request):
#     appointments = Appointment.objects.all()
#     return render(request, 'appointments/appointment_list.html', {'appointments': appointments})

# @method_decorator(login_required, name='dispatch')
class AppointmentListView(views.View):
    def get(self, request):
        appointments = Appointment.objects.all()
        return render(request, 'appointments/appointment_list.html', {'appointments': appointments})
    def post(self, request):
        pass    
   

