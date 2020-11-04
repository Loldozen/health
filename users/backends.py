from django.contrib.auth.backends import BaseBackend, ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

from users.models import Patient

"""class UserAuthenticationBackend(BaseBackend):
    def authenticate(self,request,email=None,username=None,password=None):
        if email is None or username is None or password is None:
            return
        try:
            user = Patient.objects.filter(
                Q(email=email)|Q(username=username)
            ).first()
        except Patient.DoesNotExist:
            return None
        else:
            if user.check_password(password) and user.is_active:
                return user

    def get_user(self,user_id):
        try:
            return Patient.objects.get(id=user_id)
        except Patient.DoesNotExist :
            return None"""

class UserAuthenticationBackend(ModelBackend):
    def authenticate(self,request,email=None,password=None):
        try:
            user = Patient.objects.get(email=email)
            print(user)
        except Patient.DoesNotExist:
            return None
        else:
#             if user.check_password(password) and user.is_active:
            if user.check_password(password):
                return user

    def get_user(self, user_id):
        try:
            return Patient.objects.get(id=user_id)
        except Patient.DoesNotExist:
            return None
