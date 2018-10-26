# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect


# Create your views here
from passlib.hash import pbkdf2_sha256

from random import randrange
from django.contrib.auth.decorators import login_required
from .forms import SignUpForms, login_form
#from .pipeline import save_profile
from .models import SignUp
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .backend import CustomUserAuth
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

def logged_in(request):
    title='Welcome'
    form=SignUpForms(request.POST or None)
    print (request)
    context={}
    if form.is_valid():
        instance=form.save(commit=False)
    #print (instance.email)
        instance.user_name = instance.email.split('@')[0] + str(randrange(0, 101))
        instance.password=pbkdf2_sha256.hash(instance.password)
        user ,created= User.objects.get_or_create(email=instance.email, username=instance.user_name)
        user.first_name=instance.first_name
        user.last_name=instance.last_name
        user.password=instance.password
        user.save()
        attrs={"user":user}
        data = {

            "email": instance.email,
            "password": instance.password,
            "user_name": instance.user_name,
            "first_name": instance.first_name,
            "last_name": instance.last_name,
            "fb_link": instance.fb_link,
            "phone_number": instance.phone_number,
            "college":instance.college
        }
        attrs = dict(attrs.items() |data.items())
        SignUp.objects.create(
                   **attrs
               )
       
        if form.is_valid():

           
            form.save()
            instance.save()


            context={
               
                           "uname":"your username is "  +instance.user_name             }

    return render(request, "logged_in.html",context)
def home(request):
    form=SignUpForms(request.POST or None)
    context ={
        "forms":form

    }

    return render(request, "home.html",context) 
def profile(request):
    form =SocialSignUp(request.POST or None)

    if request.method == 'POST':
        instance=form.save(commit=False)
        profile = SignUp(user=request.user,
        fb_link=instance.fb_link,college=instance.college,phone_number=instance.phone_number)
        profile.save()
        backend = request.session['partial_pipeline']['backend']
        redirect('social:complete', backend=backend)


    context={
        "forms":form
    }
    return render(request,'profile.html',context)


def user_login(request,response=None):
    print(response)
    context={}
    form=login_form(request.POST or None)
    context ={
        "forms":form
    }
    if request.method =="POST":
      if form.is_valid():
        instance = form.save(commit=False)
        email=instance.email
        password=instance.password

        user = CustomUserAuth().authenticate(email=email, password=password)


        if user ==None:
         form = SignUpForms(request.POST or None)
         context={
             "forms":form,
             "title":"register your email here",
             "email": email
         }
         return render(request, "home.html", context)
        else:
            login(request, user,backend='sideapp.backend.CustomUserAuth')
            return redirect("edit_profile")

    return render(request, "login.html", context)

@login_required
def edit_profile(request):
    user_instance = SignUp.objects.get(user=request.user)
    data = {
        "email": user_instance.email,
        "user_name": user_instance.user_name,
        "first_name": user_instance.first_name,
        "last_name": user_instance.last_name,
        "fb_link": user_instance.fb_link,
        "phone_number": user_instance.phone_number,
        "college":user_instance.college
    }
    form = SignUpForms(data, initial=data)
    context = {
        "forms": form
    }
    return render(request, "edit_profile.html", context)
@login_required
def update_profile(request):
    title='Welcome'
    form=SignUpForms(request.POST or None)
   
    instance=form.save(commit=False)


    user_object.email= instance.email
    request.user.password=pbkdf2_sha256.encrypt(instance.password,rounds=12000,salt_size=32)
    request.user.save()
    user_object.user_name= instance.user_name
    user_object.first_name= instance.first_name
    user_object.last_name= instance.last_name
    user_object.fb_link= instance.fb_link
    user_object.phone_number= instance.phone_number
    user_object.college=instance.college
    user_object.password=request.user.password
    user_object.save()
    user_instance = SignUp.objects.get(user=request.user)
    data = {
        "email": user_instance.email,
        "user_name": user_instance.user_name,
        "first_name": user_instance.first_name,
        "last_name": user_instance.last_name,
        "fb_link": user_instance.fb_link,
        "phone_number": user_instance.phone_number,
        "college":user_instance.college
    }
    form = SignUpForms(data, initial=data)
    context = {
        "forms": form
    }
    return render(request, "edit_profile.html", context)



@login_required
def user_logout(request):
    logout(request)
    return redirect('login')



