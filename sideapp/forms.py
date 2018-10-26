from django import forms
from sideapp.models import SignUp, login

class SignUpForms(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model =SignUp
        fields = ["first_name", "email","password", "last_name", "phone_number","fb_link","college"]

class login_form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=login
        fields=["email","password"]