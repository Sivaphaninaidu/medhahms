from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import google.generativeai as genai
from django.conf import settings
from doctors.models import Doctor
from patients.models import Patient 

@login_required
def dashboard_home(request):
    return render(request, 'dashboard_home.html')

@login_required
def dashboard_hms_ai(request):
    answer = None
    
    if request.method == 'POST':
        user_query = request.POST.get('query', '')
        
        if user_query:
            genai.configure(api_key=settings.GEMINI_API_KEY)
            doctors = Doctor.objects.all()
            patients = Patient.objects.all()
            
            doctors = list(doctors.values())
            patients = list(patients.values())
            
            # FIX: Use .format() to insert the actual data
            final_query = '''
You are the AI chatbot inside a website called medhaHMS.
Your responsibility is to answer questions about medhaHMS data. 
Anything apart from this, you are not allowed to answer. 

Below is the doctor data you need to know: 
{doctors} 

Below are the patients data: 
{patients}

Answer the below question:
{user_query}
            '''.format(doctors=doctors, patients=patients, user_query=user_query)
            
            model = genai.GenerativeModel('gemini-flash-latest')
            response = model.generate_content(final_query)
            answer = response.text
    
    return render(request, 'dashboard_hms_ai.html', {
        'answer': answer
    })
# AIzaSyAB4319LMsTrk1IgkkmDUTrv2latHw2ifo    
# projects/171994236309
# 171994236309
