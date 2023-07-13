from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User


class UserCreationForm(forms.ModelForm):
    pwd1=forms.CharField(label='Password',widget=forms.PasswordInput)
    pwd2=forms.CharField(label='Password confirm',widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=('name','email')
    
    def clean_pwd2(self):
        pwd1=self.cleaned_data.get("pwd1")
        pwd2=self.cleaned_data.get("pwd2")
        if pwd1 and pwd2 and pwd1!=pwd2:
            raise forms.ValidationError("비밀번호가 일치하지 않습니다.")
        return pwd2
    
    def save(self, commit=True):
        user=super().save(commit=False)
        user.set_password(self.cleaned_data["pwd1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    # 관리자 권한
    password=ReadOnlyPasswordHashField()

    class Meta:
        model=User
        fields=('name','email','password', 'profile_img','portfolio','school','bio','star','review')
    
    # def clean_password(self):
    #     return self.initial["password"]


class CustomUserChangeForm(UserChangeForm):
    # 일반 사용자 권한
    class Meta:
        model=get_user_model() # 현재 활성화된 사용자 모델을 반환
        fields=('name', 'profile_img','portfolio','school','bio','star','review')
