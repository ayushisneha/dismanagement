# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import SignUp
class SignUpAdmin(admin.ModelAdmin):
        list_display=["last_name","first_name"]
        class Meta:
            model = SignUp
admin.site.register(SignUp)