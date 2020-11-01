from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin #Permission, Group
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify

from .managers import CustomUserManager
# Create your models here.


class CustomUser(AbstractBaseUser, PermissionsMixin):
    GENDER = (
        ('Male','Male'),
        ('Female','Female'),
    )
    USER_TYPE = (
        ('Patient','Patient'),
        ('Doctor','Doctor'),
    )

    name = models.CharField(_('Full name'), max_length=100)
    slug = models.SlugField(default='slug')
    email = models.EmailField(_('Email address'), unique=True)
    gender = models.CharField(_('gender'), choices=GENDER, max_length=6)
    phone_number = models.CharField(_('Phone number'), max_length=14)
    country = models.CharField(_('Country'),max_length=50)
    state = models.CharField(_('State'),max_length=50)
    address = models.CharField(_('Address'),max_length=150)
    user_type = models.CharField(_('User Type'), choices=USER_TYPE, max_length=10, blank=True, null=True)
    is_staff = models.BooleanField(_('admin staff ?'), default=False)
    is_active = models.BooleanField(_('Active'), default=False)
    date_joined = models.DateTimeField(_('Date joined'), auto_now_add=True)
    last_login = models.DateTimeField(_('Last login'), auto_now=True)
    
    """user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="custom_user_set",
        related_query_name="custom_user",
    )
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="custom_user_set",
        related_query_name="custom_user",
    )"""

    USERNAME_FIELD = 'email'
    

    objects = CustomUserManager()

    """class Meta:
        abstract = True"""
        
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(CustomUser, self).save(*args, **kwargs)

class Patient(CustomUser):

    username = models.CharField(_('Username'), max_length=30)
    #user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    blood_group = models.CharField(_('Blood group'), max_length=10)
    genotype = models.CharField(_('Genotype'), max_length=2)
    height = models.IntegerField(_('Height(Meters)'))
    weight = models.IntegerField(_('Weight(lbs)'))
    objects = CustomUserManager()

    REQUIRED_FIELDS = ['username',]

    #class Meta:
        #unique_together = (('email','username'),)
    def save(self, *args, **kwargs):
        self.user_type = 'Patient'
        super(Patient, self).save(*args, **kwargs)