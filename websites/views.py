from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
import datetime
from django.utils import timezone
from django.shortcuts import redirect
from django.db.models.query import EmptyQuerySet
from django.template.loader import render_to_string
from .models import user, member, varsity, eventlol
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

def usercount():
    no = user.objects.count()
    return no + 1
	
def membercount():
    no = member.objects.count()
    return no + 1
	
def	eventcount():
	no=eventlol.objects.count()
	return no+1

def Homepage(request):
	vars=request.session['vnum']
	context = {'vnum': vars,'username':request.session['username']}
	print(request.session['username'])
	return render(request,'websites/homescreen.html',context)
	
def loginattempt (request):
	return render(request, 'websites/login.html')
	
def login (request):
	if (isinstance(request.POST['username'], str) and request.POST['username']!= '' and isinstance(request.POST['password'],str)and request.POST['password']!=''):
		curuser=user.objects.filter(u_username=request.POST['username']).filter(u_password=request.POST['password'])
		if (  len(curuser)==0 ):
			return render(request,'websites/login.html', {'error_message': "Invalid Credentials."})
		else:
			request.session['username']=request.POST['username']
			if(curuser.first().u_varsity==None):
				return redirect('websites:Homepage')
			else:
				request.session['vnum']=curuser.first().u_varsity
				return  redirect('websites:customize')
	else:
		return render(request,'websites/login.html', {'error_message': "Invalid Credentials."})
def logout (request):
	request.session['username']=''
	request.session['vnum']=''
	return redirect('websites:Homepage')
	
def editpage(request):
	context = {'username':request.session['username']}
	return render(request,'websites/editVarsityInfo.html',context)
	
def edit(request):
	vars=varsity.objects.get(v_num=request.session['vnum'])
	if (isinstance(request.POST['name'], str) and request.POST['name']!= ''):
		vars.v_name=request.POST['name']
	if( isinstance(request.POST['email'],str)and request.POST['email']!=''):
		vars.v_email=request.POST['email']
	if( isinstance(request.POST['contact'],str)and request.POST['contact']!=''):
		vars.v_contact=request.POST['contact']
	vars.save()
	return redirect('websites:Homepage')
	
def directory (request):
	varsities=varsity.objects.all()
	if request.method=='POST':
		if isinstance(request.POST['varsityname'],str) and request.POST['varsityname']!='':
			varsities=varsities.filter(v_name__icontains=request.POST['varsityname'])
	members=member.objects.all()
	context = {'varsities': varsities,'members': members,'username':request.session['username']}
	return render(request, 'websites/directory.html', context)

def events (request):
	dates = eventlol.objects.all()
	context = {'dates': dates,'username':request.session['username']}
	return render(request, 'websites/eventsList.html', context)
	
def descedit (request):
	vars=varsity.objects.get(v_num=request.session['vnum'])
	vars.v_desc=request.POST['description']
	vars.save()
	return redirect('websites:customize')

def adddate(request):
	return render(request,'websites/adddate.html')
	
def insertdate(request):
	vars=varsity.objects.get(v_num=request.session['vnum'])
	new =eventlol(
	e_team=vars,
	e_date=request.POST['date'],
	e_start=request.POST['start'],
	e_end=request.POST['end'],
	e_desc=request.POST['desc'],
	)
	new.save()
	return redirect('websites:edit2')
	
def insertmember(request):
	new= member(
		m_team=varsity.objects.get(v_num=request.session['vnum']),
		m_name=request.POST['name'],
		m_role=request.POST['role'],
	)
	new.save()
	return redirect('websites:edit2')
	
def newmember(request):
	return render(request,'websites/insertMembers.html')
	
def customize(request):
	vars=varsity.objects.get(v_num=request.session['vnum'])
	context = {'vars': vars,'username':request.session['username']}
	return render(request,'websites/managerPage.html',context)

def signup(request):
	return render(request,'websites/signup.html')

def register(request):
	if request.POST['password']==request.POST['cpassword'] and not user.objects.filter(u_username=request.POST['username']).exists() :
		new=user(
		u_username=request.POST['username'],
		u_password=request.POST['password']
		)
		new.save()
		return redirect('websites:Homepage')
	else:
		return render(request,'websites/signup.html')
'''
def email(request):
	vars=varsity.objects.get(v_num=request.session['vnum'])
	lol=users.objects.filter(u_varsitysubscriptions=request.session['vnum'])
	for i in lol:
		send_mail(
			request.POST['topic'],
			request.POST['content'],
			vars.v_email,
			i.u_username,
			fail_silently=False,
		)
	return redirect('websites:Homepage')
'''
def aboutus(request):
	context={'username':request.session['username']}
	return render(request,'websites/aboutus.html', context)

def contactus(request):
	context={'username':request.session['username']}
	return render(request, 'websites/contactus.html',context)
#from datetime import datetime
#datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
def myPage(request):
	#if(request.session.modified == True and request.session['username'] != None):
	users=user.objects.get(u_username=request.session['username'])
	membership=varsity.objects.filter(v_num=users.u_varsity)
	xd=users.u_varsitysubscriptions.all()
	if(len(membership)==0):
		context = {'user': users,'username':request.session['username'],'subs':xd}
	else:
		context = {'user': users,'username':request.session['username'],'subs':xd,'member':membership.first().v_name}
	return render(request, 'websites/myPage.html', context)
def changepass(request):
	if request.POST['password']==request.POST['cpassword'] and request.POST['password'] != None:
		users=user.objects.get(u_username=request.session['username'])
		users.u_password=request.POST['password']
		users.save()		
	return redirect('websites:myPage')
	
def send_email(request):
	vars=varsity.objects.get(v_num=request.session['vnum'])
	if isinstance(request.POST['subject'], str) and request.POST['subject']!= '' and isinstance(request.POST['content'],str)and request.POST['content']!='' and vars.v_email != None:
		subject=request.POST['subject']
		message=request.POST['content']
		curuser=user.objects.filter(u_varsitysubscriptions=request.session['vnum'])
	#	for object in curuser:
	#		send_mail(subject, message, vars.v_email, [object.u_username])
			
		return redirect('websites:customize')
	else:
        # In reality we'd use a form class
        # to get proper validation errors.
		return redirect('websites:Homepage')
		
def varsitee(request, vnum):
	request.session['varsityseen']=vnum
	vars=varsity.objects.get(v_num=vnum)
	context = {'vars': vars,'username':request.session['username']}
	return render (request,'websites/varsity.html',context)
	
def varsitee2(request, vnum):
	request.session['varsityseen']=vnum
	vars=varsity.objects.get(v_num=vnum)
	context = {'vars': vars,'username':request.session['username']}
	return render (request,'websites/varsity2.html',context)
	
def varsitee3(request, vnum):
	dates = eventlol.objects.filter(e_team=vnum)
	request.session['varsityseen']=vnum
	vars=varsity.objects.get(v_num=vnum)
	context = {'vars': vars,'username':request.session['username'],'dates': dates}
	return render (request,'websites/varsity3.html',context)
	
def subscribe(request,vnum):
	xd=user.objects.get(u_username=request.session['username'])
	var=varsity.objects.get(v_num=vnum)
	xd.u_varsitysubscriptions.add(vnum)
	xd.save()
	return redirect('websites:varsitee', vnum)
	
def edit2(request):
	vars=varsity.objects.get(v_num=request.session['vnum'])
	context = {'vars': vars,'username':request.session['username']}
	return render(request,'websites/managerpage2.html',context)
	
def subscriptions(request):
	users=user.objects.get(u_username=request.session['username'])
	
	list=[]
	for i in users.u_varsitysubscriptions.all():
		list+= eventlol.objects.filter(e_team=i)
	print (list)
	context={'username':request.session['username'],'dates':list,'subs':users.u_varsitysubscriptions.all()}
	
	return render(request,'websites/subscribe.html',context)