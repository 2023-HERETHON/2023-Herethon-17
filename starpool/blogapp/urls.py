from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blogapp import views

app_name = "blog"

urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('comment/<int:id>/', views.commentBox, name='commentBox'),
    path('detail/<int:id>/<int:comment_id>/', views.comment_detail, name='comment_detail'),
    path('commentReview/', views.comment_review, name='comment_review'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)