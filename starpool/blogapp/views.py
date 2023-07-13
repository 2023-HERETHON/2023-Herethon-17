from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.http import HttpResponse

def home(request):
    posts = Post.objects.all().order_by('-id') # admin에서 생성한 공모전 post 개체 생성 
    return render(request, 'mainpage.html', {'posts':posts})

def detail(request, id):
    # pk값이 id인 Post 객체 하나를 가져와 post라는 변수에 담아줌
    post = get_object_or_404(Post, pk=id)
    context = {
        'post' : post
    }
    return render(request, 'listpage.html', context)


