from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model, authenticate
from django.core.exceptions import ValidationError

from .models import Patient

class PatientSignupForm(UserCreationForm):

    #def __init__(self, *args, **kwargs):
        #super(DoctorSignupForm, self).__init__(*args, **kwargs)
    
    class Meta:
        model = Patient
        fields = ('name','username','email','gender','phone_number','country','state','address','blood_group','genotype','height','weight')
        #exclude = ('is_staff','is_active','date_joined','last_login',)


class PatientUpdateForm(UserChangeForm):

    class Meta:
        model = Patient
        fields = ('name','username','email','gender','phone_number','country','state','address','blood_group','genotype','height','weight')
        #exclude = ('is_staff','is_active','date_joined','last_login',)

class PatientLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
