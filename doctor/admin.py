from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.apps import apps

from .forms import DoctorSignupForm, DoctorUpdateForm
from .models import Doctor

# Register your models here.

class DoctorAdmin(admin.ModelAdmin):
    add_form = DoctorSignupForm
    form = DoctorUpdateForm
    model = Doctor
    list_display = ('mdcn','email','name','last_login','is_staff','is_active')
    list_filter = ('mdcn','email','name','last_login','is_staff','is_active')
    fieldset = (
        (None, {'fields':('mdcn','email','phone_number','name','password')}),
        ('Permissions',{'fields': ('is_staff','is_active')}),
    )
    add_fieldset = (
        (None,{
            'classes':('wide',),
            'fields':('mdcn','email','name','phone_number','password1','password2','is_staff','is_active')
        }
         ),
    )
    search_fields = ('name',)
    readonly_fields = ('date_joined','last_login',)
    ordering = ('mdcn','name')

admin.site.register(Doctor, DoctorAdmin)