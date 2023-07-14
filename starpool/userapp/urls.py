from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('signup/',signup, name='signup'),
    path('login/',login, name='login'),
    path('logout/',logout,name='logout'),
    path('myinfo/<int:user_id>/',myinfo,name='myinfo'),
    path('update/<int:user_id>/',update,name='update'),
    path('changepwd/<int:user_id>/',change_password,name='change_password'),
]
