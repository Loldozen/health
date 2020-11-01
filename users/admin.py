"""from django.contrib import admin
from users.models import CustomUser
# Register your models here.

admin.site.register(CustomUser)"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.apps import apps

from .forms import PatientSignupForm, PatientUpdateForm
from .models import Patient

# Register your models here.

class PatientAdmin(admin.ModelAdmin):
    first_name = None
    last_name = None
    add_form = PatientSignupForm
    form = PatientUpdateForm
    model = Patient
    list_display = ('username','email','name','last_login','is_staff','is_active')
    list_filter = ('username','email','name','last_login','is_staff','is_active')
    fieldset = (
        ('Personal Details', {'fields':('username','email','phone_number','name','password')}),
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
    ordering = ('date_joined','name','last_login')

admin.site.register(Patient, PatientAdmin)