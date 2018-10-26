from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class City(models.Model):
    cityname = models.CharField(max_length=50)
    status = models.CharField(max_length=50, default=None, blank=True)
    distype = models.CharField(max_length=50, default=None, blank=True)

    def __str__(self):
        return self.cityname

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    cityname = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
