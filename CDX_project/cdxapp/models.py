from django.db import models
from django.contrib.auth.signals import user_logged_in, user_logged_out  
from django.contrib.auth.models import User
import urllib, hashlib, binascii
from datetime import datetime

def hash_username(username):
	heashed = binascii.crc32(username)
	return heashed

class AppUser(models.Model):
	userID = models.IntegerField()
	fname = models.CharField(max_length=300)
	lname = models.CharField(max_length=300)
	balance = models.FloatField(default=0.0)
	def __unicode__(self):
		return self.fname

class Message(models.Model):
	message = models.TextField(max_length=200)
	def __unicode__(self):
		return self.message

class AppU(models.Model):
	user = models.OneToOneField(User)
	userID =  models.IntegerField()
	username = models.CharField(max_length=300)
	is_app_user = models.BooleanField(default=False)
	last_accessed = models.DateTimeField(auto_now_add=True)
	
User.profile = property(lambda u: AppU.objects.get_or_create(user=u,defaults={'username':u.username,'userID':hash_username(u.username)})[0])
