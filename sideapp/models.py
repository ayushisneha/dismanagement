# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
#from passlib.hash import pbkdf2_sha256

# Create your models here.
class SignUp(models.Model):
    user = models.ForeignKey(User,null=True,on_delete=models.PROTECT)
    email=models.EmailField(null=True,blank=True,unique=True)
    password = models.CharField(max_length=100)
    user_name=models.CharField(max_length=120,blank=True,null=True)
    first_name=models.CharField(max_length=120,blank=True,null=True,default='')
    last_name=models.CharField(max_length=120,blank=True,null=True,default='')
    phone_number=models.CharField(max_length=12,blank=True,null=True)
    college=models.CharField(max_length=120, blank=True ,null=True)
    fb_link=models.CharField(max_length=120,blank=True,null=True,default='')
    time=models.DateTimeField(auto_now_add=True,auto_now=False,null=True)
    updated=models.DateTimeField(auto_now_add=False,auto_now=True,null=True)

    def __str__(self):
         return self.user.username

class login(models.Model):
    email = models.EmailField()
    password=models.CharField(max_length=100)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#         instance.SignUp.save()
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#        profile, created = SignUp.objects.get_or_create(user=instance)
#
# post_save.connect(create_user_profile, sender=User)
#
