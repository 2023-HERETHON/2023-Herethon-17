from django.contrib import admin
from django.urls import path, include
from blogapp import views

app_name = "blog"

urlpatterns = [
    path('', views.home, name='home'),
    path('post/', views.post, name='post'),
    path('detail/', views.detail, name='detail'),
    
]