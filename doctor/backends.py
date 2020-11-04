from django.contrib.auth.backends import BaseBackend, ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

from doctor.models import Doctor

class DoctorAuthenticationBackend(BaseBackend):
    def authenticate(self,request,mdcn=None,password=None):
        if mdcn is None or password is None:
            return
        try:
            doctor = Doctor.objects.get(mdcn=mdcn)
        except Doctor.DoesNotExist:
            return
        else:
            if doctor.check_password(password) and doctor.is_active:
                return doctor

    def get_user(self,doctor_id):
        try:
            return Doctor.objects.get(id=doctor_id)
        except Doctor.DoesNotExist:
            return None
