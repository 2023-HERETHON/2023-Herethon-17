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


def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        user=authenticate(request,email=email, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('test')
        else:
            # 로그인 실패 시
            return render(request, 'login.html',{'error':'user info is not correct'})
    
    else:
        # GET 메소드일 시
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('test')

def test(request):
    return render(request,'test.html')