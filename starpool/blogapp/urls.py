from django.contrib import admin
from django.urls import path, include
from blogapp import views

app_name = "blog"

urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<int:id>/', views.detail, name='detail'),
    
]