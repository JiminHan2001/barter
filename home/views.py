import json

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout



# Create your views here.
def home(request):
    return render(request, 'home/home.html', {})

"""def user_login(request):
    msg = "login입니다."
    return render(request, 'home/user_login.html',{'message': msg})

def user_register(request):
    msg = "회원가입입니다."
    return render(request, 'home/user_register.html', {'message': msg})"""

def user_register(request):
    if request.method == "POST":
        if request.POST.get("password1","") == request.POST.get("passdword2",""):
            user = User.objects.create_user(
                username=request.POST["username"], password=request.POST["password1"])
            auth.login(request,user)
            return redirect('home')
        return render(request, 'home/user_register.html')

    return render(request, 'home/user_register.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'user_login.html', {'error': 'username or password is incorrect'})
    else:
        return render(request, 'user_login.html')

def logout(request):
    auth_logout(request)
    return redirect('home')
