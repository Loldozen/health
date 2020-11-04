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

    def __init__(self, *args, **kwargs):
        """
        The 'request' parameter is set for custom auth use by subclasses.
        The form data comes in via the standard 'data' kwarg.
        """
        self.request = kwargs.get("request")
        self.user_cache = None
        super().__init__(*args, **kwargs)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            self.user_cache = authenticate(self.request, email=email, password=password)
            if self.user_cache is None:
                raise ValidationError("Invalid Username or Password")
            if not self.user_cache.is_active:
                raise ValidationError("User Account is not activated")

        return self.cleaned_data

    def save(self):
        return self.user_cache
