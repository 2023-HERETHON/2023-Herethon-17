# Generated by Django 4.2.3 on 2023-07-14 14:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='제목')),
                ('image', models.ImageField(blank=True, upload_to='postImage', verbose_name='이미지')),
                ('date', models.DateField(verbose_name='기간')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_pw', models.CharField(default=None, max_length=4, verbose_name='리뷰코드')),
                ('review', models.TextField(max_length=100, verbose_name='리뷰')),
                ('writer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
            ],
        ),
        migrations.CreateModel(
            name='CommentBox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=500, verbose_name='내용')),
                ('comment_pw', models.CharField(default=None, max_length=4, verbose_name='평가코드')),
                ('date', models.DateField(auto_now_add=True, verbose_name='작성일')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blogapp.post', verbose_name='포스트')),
                ('writer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
            ],
        ),
    ]
