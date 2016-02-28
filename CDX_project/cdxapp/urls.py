from django.conf.urls import patterns, url, include
from cdxapp import views
from django.contrib import admin

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
	url(r'^login', views.login, name='login'),
	url(r'^logout', views.logout, name='logout'),
        url(r'^about/', include(admin.site.urls)))
