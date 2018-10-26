from django.db import models
from django.contrib.auth.models import User
# Create your models here.


city_choices = [
        ('Chennai', 'Chennai'),
        ('Delhi', 'Delhi'),
        ('Bombay', 'Bombay'),
        ('Tirupati', 'Tirupati'),
        ('Agra','Agra'),
]

alert_choices=[
    ('Forest_Fire', 'Forest_Fire'),
    ('Flood', 'Flood'),
    ('tora', 'tora'),
]

status_choices=[
    ('Safe', 'Safe'),
    ('Unsafe', 'Unsafe'),
]
#
# class City(models.Model):
# 	city_name=models.CharField(choices = city_choices,max_length=130, null=True, blank=True)
# 	status = models.BooleanField(default=False)
# 	unsafe_peoples=models.BigIntegerField(null=True, blank=True)
# 	def __str__(self):
# 		return self.city_name
#

class UserProfileInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    city  = models.CharField(choices = city_choices,max_length=130, null=True, blank=True)

    def __str__(self):
        return self.user.username

#test models


class City(models.Model):
    city_name=models.CharField(choices = city_choices,max_length=130, null=True, blank=True)

    #alert_name= models.ManyToMany(Alert)
    #unsafe_peoples=models.BigIntegerField(null=True, blank=True)

    def __str__(self):
        return self.city_name


class Alert(models.Model):
    city_name=models.ForeignKey(City,on_delete=models.CASCADE)
    alert_name = models.CharField(choices=alert_choices, max_length=130, null=True, blank=True)
    unsafe_peoples = models.BigIntegerField(null=True, blank=True,default =0)


    def __str__(self):
        return  self.alert_name


class Report(models.Model):
    alert_name = models.CharField(choices=alert_choices, max_length=130, null=True, blank=True)
    status = models.CharField(choices=status_choices, max_length=130, null=False, blank=False)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.status
