from .models import SignUp
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from passlib.hash import pbkdf2_sha256

class CustomUserAuth(object):

    def authenticate(self, email=None, password=None):
        try:
              user = User.objects.get(email=email)
        except User.DoesNotExist:
            return None
        if pbkdf2_sha256.verify(password, user.password):
            return user
        return None
    def get_user(self, user_id):
        try:
            user = User.objects.get(pk=user_id)
            if user.is_active:
                return user
            return None
        except User.DoesNotExist:
            return None
