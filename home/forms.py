from django import forms
from home.models import UserProfileInfo
from django.contrib.auth.models import User
from .models import Report

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'password', 'email')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic', 'city')


class ReportForm(forms.ModelForm):
    class Meta():
        model = Report
        fields = ('alert_name', 'status')


