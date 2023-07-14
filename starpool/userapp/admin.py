from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserChangeForm, UserCreationForm
from .models import User

class UserAdmin(BaseUserAdmin):
    form=UserChangeForm
    add_form=UserCreationForm

    list_display=('name','email','profile_img','portfolio','school','bio','star','review','is_admin')
    list_filter=('is_admin',)
    fieldsets=(
        (None, {'fields':('email','password')}),
        ('User info',{'fields':('name','profile_img','portfolio','school','bio','star','review')}),
        ('Permissions',{'fields':('is_admin',)})
    )

    add_fieldsets=(
        (None,{
            'classes':('wide',),
            'fields':('email','name','password1','password2')
        })
    )
    search_fields=('email',)
    ordering=('email',)
    filter_horizontal=()

admin.site.register(User,UserAdmin)
admin.site.unregister(Group)
