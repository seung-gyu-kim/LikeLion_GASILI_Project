from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # add page
    add_form = CustomUserCreationForm
    add_fieldsets = (
        ('ID & PASSWORD', {'fields': ('username', 'password1', 'password2')}),
        ('NAME', {'fields': ('first_name', 'last_name')}),
        ('PERSONAL INFO', {'fields': ('gender', 'birthdate')}),
        ('PERMISSIONS', {'fields': ('is_active', 'is_staff', 'is_superuser')})
    )
     
    # change page
    form = CustomUserChangeForm
    fieldsets = (
        ('ID & PASSWORD', {'fields': ('username', 'password')}),
        ('NAME', {'fields': ('first_name', 'last_name')}),
        ('PERSONAL INFO', {'fields': ('gender', 'birthdate')}),
        ('PERMISSIONS', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    
    # list page
    list_display = ['username', 'first_name', 'last_name', 'gender', 'birthdate']

admin.site.register(CustomUser, CustomUserAdmin)