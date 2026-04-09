from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request, 'users/signup.html', {
                'error': 'Username already exists'
            })

        user = User.objects.create_user(username=username, password=password)
        user.save()

        return redirect('dashboard')

    return render(request, 'users/signup.html')   # 👈 HERE


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('/dashboard/')   # ✅ ONLY redirect

    return render(request, 'users/user_login.html')   # ✅ ONLY login page


def user_logout(request):
    logout(request)
    return redirect('/login')   