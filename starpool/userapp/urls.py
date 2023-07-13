from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('signup/',signup, name='signup'),
    path('login/',login, name='login'),
    path('logout/',logout,name='logout'),
    path('myinfo/',myinfo,name='myinfo'),
    path('update/',update,name='update'),
]
