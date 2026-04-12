from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
import resend
from django.conf import settings




def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        if User.objects.filter(username=username).exists():
            return render(request, 'users/signup.html', {
                'error': 'Username already exists'
            })

        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()

        resend.api_key = settings.RESEND_API_KEY
        resend.Emails.send(
            {
                'from': 'onboarding@resend.dev',
                'to': ['sivaphaninaidu999@gmail.com'],
                "subject": 'Welcome to HMS',
                "html": f'<h1>Welcome {user.username}</h1>'
            }
        )

        return redirect('dashboard')

    return render(request, 'users/signup.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if user.email:
               return redirect('/dashboard/')

    return render(request, 'users/user_login.html')


def user_logout(request):
    logout(request)
    return redirect('/login')