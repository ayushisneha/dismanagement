from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^lost$', views.lost, name='lost'),
    url(r'^found$', views.found, name='found'),
]