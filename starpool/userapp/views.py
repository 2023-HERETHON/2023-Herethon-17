from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth import authenticate
from .models import User
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserChangeForm
from django.contrib.auth.hashers import check_password
from django.contrib import messages,auth
from django.contrib.auth import get_user_model
from blogapp.models import *

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
            return redirect('blog:home')
        else:
            # 로그인 실패 시
            return render(request, 'login.html',{'error':'user info is not correct'})
    
    else:
        # GET 메소드일 시
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('blog:home')


def myinfo(request, user_id):
    login_user=get_user_model()
    user=get_object_or_404(login_user, pk=user_id)
    com_box=CommentBox.objects.filter(writer=user).order_by('id')

    context={
        'user':user,
        'com_box':com_box
    }
    return render(request,'myinfo.html',context)


def update(request, user_id):
    if request.method=='POST':
        # request.FILES는 이미지 업로드 할 때 사용
        form=CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('myinfo',user_id)
    else:
        form=CustomUserChangeForm(instance=request.user)
    
    context={
        'form':form,
    }
    return render(request, 'update.html',context)

def change_password(request, user_id):
    if request.method=='POST':
        user=request.user
        origin_password=request.POST['origin_password']
        if check_password(origin_password,user.password):
            password1=request.POST["password1"]
            password2=request.POST["password2"]

            if password1==password2:
                user.set_password(password1)
                user.save()
                auth.login(request,user)
                return redirect('myinfo',user_id)
            else:
                messages.error(request,'비밀번호가 일치하지 않습니다.')
        
        else:
            messages.error(request,'비밀번호가 맞지 않습니다.')
    
    return render(request,'change_password.html')
