from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from doctor.models import Doctor 

class DoctorSignupForm(UserCreationForm):

    #def __init__(self, *args, **kwargs):
        #super(DoctorSignupForm, self).__init__(*args, **kwargs)
    LANGUAGES = (
        ('English','English'),
        ('Yoruba','Yoruba'),
        ('Igbo','Igbo'),
        ('Hausa','Hausa'),
        ('Fulfulde','Fulfulde'),
        ('Tiv','Tiv'),
        ('Nupe','Nupe'),
        ('Kanuri','Kanuri'),
        ('Ibibio','Ibibio'),
        ('French','French'),
        ('Spanish','Spanish'),
        ('Chinese','Chinese'),
    )
    language = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=LANGUAGES)

    class Meta:
        model = Doctor
        fields = ('name','email','phone_number','mdcn','specialization','language')

class DoctorUpdateForm(UserChangeForm):

    LANGUAGES = (
        ('English','English'),
        ('Yoruba','Yoruba'),
        ('Igbo','Igbo'),
        ('Hausa','Hausa'),
        ('Fulfulde','Fulfulde'),
        ('Tiv','Tiv'),
        ('Nupe','Nupe'),
        ('Kanuri','Kanuri'),
        ('Ibibio','Ibibio'),
        ('French','French'),
        ('Spanish','Spanish'),
        ('Chinese','Chinese'),
    )
    language = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=LANGUAGES)

    class Meta:
        model = Doctor
        fields = ('name','email','phone_number','mdcn','specialization','language')