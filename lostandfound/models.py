from django.db import models


class Lost(models.Model):
    name = models.CharField(max_length=50, blank=False)
    address = models.CharField(max_length=50)
    pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.name


class Found(models.Model):
    name = models.CharField(max_length=50, blank=False)
    address = models.CharField(max_length=50, blank=True)
    pic = models.ImageField(upload_to='profile_pics', blank=True)
    location = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name

