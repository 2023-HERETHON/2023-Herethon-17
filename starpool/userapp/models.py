from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

class UserManager(BaseUserManager):
    def create_user(self, email,name, password=None):
        if not email:
            raise ValueError('이메일을 작성해주세요.')
        
        if not name:
            raise ValueError('이름을 작성해주세요.')

        user=self.model(
            name=name,
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, password):
        user=self.create_user(
            email,
            name=name,
            password=password
        )
        user.is_admin=True
        user.save(using=self._db)
        return user


choice=(
    (0,'False'),
    (1,'True')
)

class User(AbstractBaseUser):
    name=models.CharField(max_length=30)
    email=models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    profile_img=models.ImageField(upload_to = "pf_img/", null=True, blank=True)
    portfolio=models.FileField(upload_to = "pofol/", null=True, blank=True)
    school=models.CharField(max_length=30, blank=True, default='')
    bio=models.CharField(max_length=500, blank=True, default='')
    star=models.SmallIntegerField(choices = choice, default=1)
    review=models.SmallIntegerField(choices = choice, default=1)
    is_active=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)

    objects=UserManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name']

    def __str__(self):
        return self.email
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin