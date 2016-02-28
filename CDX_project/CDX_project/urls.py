from django.conf.urls import patterns, include, url
from django.contrib import admin
from cdxapp import views

urlpatterns = patterns('',
    url(r'^admin/', views.admin, name='admin'),                       
    url(r'^cdxapp/', include('cdxapp.urls')),
    url(r'^$', include('cdxapp.urls')),)
