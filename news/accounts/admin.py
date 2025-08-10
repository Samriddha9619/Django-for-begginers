from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.

from .forms import Cucf,Cuchangef
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form=Cucf
    form=Cuchangef
    model=CustomUser
    list_display=[
        "email",
        "username",
        "age",
        "is_staff",
    ]
    fieldsets= UserAdmin.fieldsets + ((None,{"fields":("age",)}),)
    add_fieldsets= UserAdmin.fieldsets + ((None,{"fields": ("age",)}),)

admin.site.register(CustomUser,CustomUserAdmin) 