from django.db import models
from userapp.models import User
#from django.core.validators import MinValueValidator, MaxValueValidator

class Post(models.Model):
    title = models.CharField(verbose_name="제목", max_length=30)
    image = models.ImageField(verbose_name="이미지", blank=True, null=True, upload_to='postImage')
    date = models.DateField(verbose_name="기간")
    
    def __str__(self) :
        return str(self.title) 
    
#평가창입력
class CommentBox(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="포스트", null=True)
    content = models.TextField(verbose_name="내용", max_length=500)
    # 패스워드 4자리(무조건 입력)
    comment_pw = models.CharField(verbose_name="평가코드", max_length=4, default=None)
    # auto_now_add <= 최초 작성 시간
    date = models.DateField(verbose_name="작성일", auto_now_add=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="작성자",null=True)

    def __str__(self) :
        return str(self.content)

#팀원평가    
class Review(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="포스트", null=True)
    comment = models.ForeignKey(CommentBox, on_delete=models.CASCADE, verbose_name="댓글", null=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="작성자",null=True)
    rating = models.IntegerField(null=True)
    review_pw = models.CharField(verbose_name="리뷰코드", max_length=4, default=None)
    review = models.TextField(verbose_name="리뷰",  max_length=100)

    def __str__(self) :
        return str(self.review)
