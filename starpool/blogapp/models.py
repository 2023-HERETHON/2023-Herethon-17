from django.db import models

class Post(models.Model):
    title = models.CharField(verbose_name="제목", max_length=30)
    image = models.ImageField(verbose_name="이미지", blank=True, upload_to='postImage')
    date = models.DateField(verbose_name="기간")
    
    def __str__(self) :
        return str(self.title) 