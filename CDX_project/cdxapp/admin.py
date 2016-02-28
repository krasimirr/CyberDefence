from django.contrib import admin
from cdxapp.models import Message, AppUser

class Auser(admin.ModelAdmin):
    list_display = ('userID', 'fname', 'lname', 'balance')

admin.site.register(AppUser, Auser)
admin.site.register(Message)
