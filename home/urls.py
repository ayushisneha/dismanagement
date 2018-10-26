from django.conf.urls import url
from home import views
# SET THE NAMESPACE!
app_name = 'home'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^user_status/$', views.user_status, name='user_status'),
    url(r'^update_status/$', views.report, name='report'),
    url(r'^disaster/$', views.disaster, name='disaster'),
]
