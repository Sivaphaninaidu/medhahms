from django.shortcuts import render
from django.http import HttpResponse
from .models import Doctor
from django.contrib.auth.decorators import login_required

@login_required
def doctors_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors/list.html', {'doctors': doctors})

def home(request):
    return HttpResponse("Doctors Home Page")