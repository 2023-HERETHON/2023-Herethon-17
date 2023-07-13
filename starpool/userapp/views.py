from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth import authenticate
from .models import User
from django.shortcuts import render, redirect

def signup(request):
    if request.method=='POST':
        if request.POST['password1']==request.POST['password2']:
            user=User.objects.create_user(
                email=request.POST['email'],
                name=request.POST['name'],
                password=request.POST['password1']
            )
            auth.login(request, user)
            return redirect('/')
        
    return render(request, 'signup.html')