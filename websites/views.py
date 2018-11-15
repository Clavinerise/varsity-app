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
from django.core.mail import send_mai

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
	if(request.session.modified == True):
		vars=request.session['vnum']
		context = {'vnum': vars}
	return render(request,'websites/Homepage.html')
	
def loginattempt (request):
	return render(request, 'websites/login-screen/login.html')
	
def login (request):
	if (isinstance(request.POST['username'], str) and request.POST['username']!= '' and isinstance(request.POST['password'],str)and request.POST['password']!=''):
		curuser=user.objects.filter(u_username=request.POST['username']).filter(u_password=request.POST['password'])
		print(user.objects.none() )
		if (  len(curuser)==0 ):
			return render(request,'websites/login-screen/login.html', {'error_message': "Invalid Credentials."})
		else:
			if(curuser.first().u_varsity==None):
				return redirect('websites:Homepage')
			else:
				request.session['vnum']=curuser.first().u_varsity
				return  redirect('websites:customize')
	else:
		return render(request,'websites/login-screen/login.html', {'error_message': "Invalid Credentials."})
		
def editpage(request):
	return render(request,'websites/editpage.html')
	
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
	context = {'varsities': varsities,'members': members}
	return render(request, 'websites/directory.html', context)

def events (request):
	dates = eventlol.objects.all()
	context = {'dates': dates}
	return render(request, 'websites/events.html', context)

def adddate(request):
	return render(request,'websites/adddate.html')
	
def insertdate(request):
	vars=varsity.objects.get(v_num=request.session['vnum'])
	new =eventlol(
	e_team=vars,
	e_date=request.POST['date'],
	e_start=request.POST['start'],
	e_end=request.POST['end'],
	)
	new.save()
	return redirect('websites:Homepage')
	
def insertmember(request):
	new= member(
		m_team=varsity.objects.get(v_num=request.session['vnum']),
		m_name=request.POST['name'],
		m_role=request.POST['role'],
	)
	new.save()
	return redirect('websites:Homepage')
	
def newmember(request):
	return render(request,'websites/newmember.html')
	
def customize(request):
	return render(request,'websites/customize.html')
def signup(request):
	return render(request,'websites/signup-screen/signup.html')
def register(request):
	if request.POST['password']==request.POST['cpassword'] and not user.objects.filter(u_username=request.POST['username']).exists() :
		new=user(
		u_username=request.POST['username'],
		u_password=request.POST['password']
		)
		new.save()
		return redirect('websites:Homepage')
	else:
		return render(request,'websites/signup-screen/signup.html')
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
#from datetime import datetime
#datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
