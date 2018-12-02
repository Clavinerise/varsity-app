import datetime
from django.core.validators import RegexValidator
from django.db import connection, models
from django.utils import timezone

# Create your models here.
class user(models.Model):
	u_username=models.CharField(max_length=255,primary_key=True)
	u_password=models.CharField(max_length=255)
	u_varsity=models.IntegerField(null=True)
	u_varsitysubscriptions=models.IntegerField(null=True)
	def __int__(self):
		return u_username
	
class varsity(models.Model):
	v_num=models.IntegerField(primary_key=True)
	v_name=models.CharField(max_length=255)
	v_email=models.CharField(max_length=255,null=True)
	v_contact=models.CharField(max_length=255,null=True)
	v_file=models.FileField(blank=True, null=True, upload_to="files/%v_num")
	def __int__(self):
		return v_num
	
class member(models.Model):
	m_team=models.ForeignKey(varsity, on_delete = models.CASCADE, related_name='members')
	m_name=models.CharField(max_length=255)
	m_role=models.CharField(max_length=255)
	
class eventlol(models.Model):
	e_team=models.ForeignKey(varsity, on_delete = models.CASCADE, related_name='dates')
	e_date=models.CharField(max_length=255,null=True)
	e_start=models.CharField(max_length=255,null=True)
	e_end=models.CharField(max_length=255,null=True)
	e_desc=models.CharField(max_length=255,null=True)
	#e_date=models.DateField(null=True, blank=True)
	#e_start=models.TimeField(null=True, blank=True)
	#e_end=models.TimeField(null=True, blank=True)
