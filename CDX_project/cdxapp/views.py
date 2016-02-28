from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from cdxapp.models import AppUser, Message
from django.contrib.auth.models import User, Permission
import datetime
from django.utils.timezone import now as utcnow
from django.contrib.auth import models
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

def admin(request):
    return render(request,'cdxapp/admin.html')

def index(request):

    context={}
    if request.method == "POST":
        m = request.POST.get('message','')
        if m != '' and block(m):
            msg = Message(message=m)
            msg.save()

    if request.user.username and request.user.profile.is_app_user:
        msg = Message.objects.all()
        if msg != []:
            for m in msg:
                context[m]=m

        det = AppUser.objects.all()


        detl = []
        for d in det:
            detl.append("___________________")
            detl.append("UserID: "+str(d.userID))
            detl.append("First name: "+str(d.fname))
            detl.append("Last name: "+str(d.lname))
            detl.append("Balance: "+str(d.balance))
   
        return render(request, 'cdxapp/index.html', {'data': context.iteritems(), 'detdict': detl})
    else:
	return HttpResponseRedirect(reverse('login'))

def block(r):
    if "select" in r.lower() and "from" in r.lower():
        return False
    if "select" in r.lower() and "where" in r.lower():
        return False
    if "from" in r.lower() and "where" in r.lower():
        return False
    if "delete" in r.lower() and "where" in r.lower():
        return False
    if "delete" in r.lower() and "from" in r.lower():
        return False
    if "script" in r.lower():
        return False
    if "or" in r.lower() and "=" in r.lower():
        return False
    if "and" in r.lower() and "=" in r.lower():
        return False
    if "link" in r.lower():
        return False
    if "iframe" in r.lower():
        return False
    else:
        return True
    
def login(request):
    if request.user.username and request.user.profile.is_app_user:
        return HttpResponseRedirect(reverse('index'))
    context = {'error':'','messages':''}
    

    if request.method == 'POST':
        username = request.POST.get('username','') #return '' if no username
        password = request.POST.get('password','')

	user = auth.authenticate(username=username,password=password)

	if user is not None:
	    auth.login(request,user)
	    cu = request.user.profile
	    cu.is_app_user = True
	    cu.save()
	    return HttpResponseRedirect(reverse('index'))
	else:
	    context['error'] = 'Wrong username and/or password. Try again.'
	    return render(request,'cdxapp/login.html',context)


    
    msg = Message.objects.all()
    ml=[]
    if msg != []:
        for m in msg:
            ml.append(m)
            context['messages']=ml
    context.update(csrf(request))
    return render(request, 'cdxapp/login.html', context)

def logout(request):
    cu = request.user.profile
    cu.is_app_user = False
    cu.save()
    return render(request,'cdxapp/logout.html')
