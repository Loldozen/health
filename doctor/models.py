from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager, AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify

from ohealth import settings
from users.models import CustomUser
from users.managers import CustomUserManager
#from .managers import DoctorManager
# Create your models here.

class Doctor(CustomUser):
    
    SPECIALIZATION = (
        ('Cardiologist','Cardiologist'),
        ('Dental specialist','Dental specialist'),
        ('Dermatologist','Dermatologist'),
        ('Endocrinologist','Endocrinologist'),
        ('family medicine','family medicine'),
        ('Gastroenterology & Hepatologist','Gastroenterology & Hepatologist'),
        ('General Dentist','General Dentist'),
        ('General medicine','General medicine'),
        ('Geriatrician','Geriatrician'),
        ('Hematology','Hematology'),
        ('Infectious disease','Infectious disease'),
        ('Nephrologist','Nephrologist'),
        ('Neurologist','Neurologist'),
        ('Nuclear Physician ','Nuclear Physician '),
        ('Oncologist','Oncologist'),
        ('Ophthalmologist','Ophthalmologist'),
        ('Paediatrician','Paediatrician'),
        ('Pain physician','Pain physician'),
        ('Radiologist','Radiologist'),
        ('Radiotherapist','Radiotherapist'),
        ('Rheumatologist','Rheumatologist'),
        ('Urologist','Urologist'),
        ('Cardiothoracic & vascular surgery','Cardiothoracic & vascular surgery'),
        ('Dental Surgeon','Dental Surgeon'),
        ('ENT surgeon','ENT surgeon'),
        ('General surgeon','General surgeon'),
        ('Neurosurgeon','Neurosurgeon'),
        ('Orthopedics & Trauma surgeon','Orthopedics & Trauma surgeon'),
        ('Paediatric surgeon','Paediatric surgeon'),
        ('Plastic & Cosmetic Surgeon','Plastic & Cosmetic Surgeon'),
        ('Obstetrics & Gynecologist','Obstetrics & Gynecologist'),
        ('Psychiatrist','Psychiatrist'),
    )
    """LANGUAGES = (
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
    )"""

    #user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    mdcn = models.IntegerField(_('MDCN Number'), unique=True)
    specialization = models.CharField(_('Specialization'), choices=SPECIALIZATION,max_length=50)
    language = models.CharField(_('Languages you can consult with'), max_length=50)
    agreement = models.BooleanField(_('terms and conditions'), default=False)
    objects = CustomUserManager()
    

    #class Meta:
        #unique_together = (('mdcn','email'),)
        

    @property
    def get_mdcn(self):
        return 'The MDCN of %s is %s' %(self.name, self.mdcn)
    def save(self, *args, **kwargs):
        self.user_type = 'Doctor'
        super(Doctor, self).save(*args, **kwargs)