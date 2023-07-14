from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Post
from userapp.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, CommentBox, Review
from django.http import HttpResponse

def home(request):
    posts = Post.objects.all().order_by('-id') # admin에서 생성한 공모전 post 개체 생성 
    return render(request, 'mainpage.html', {'posts':posts})

def detail(request):
    return render(request, 'postDetail.html')


