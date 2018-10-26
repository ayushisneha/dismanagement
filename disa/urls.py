from django.urls import path
from django.conf.urls import url, include
from django.contrib import admin
from sideapp.views import home, logged_in, user_login, edit_profile, update_profile, user_logout
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login$', user_login, name='login'),
    url(r'^logout', user_logout, name='logout'),
    url(r'^logged_in',logged_in,name='logged_in'),
    url(r'^edit_profile', edit_profile, name='edit_profile'),
    url(r'^update_profile', update_profile, name='update_profile'),
    url(r'^$',home,name='home'),
]
