from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
	user		= models.OneToOneField(User)
	address		= models.TextField(blank=True)
	birthday	= models.DateField(blank=True)
	email2		= models.EmailField(blank=True)
	phone		= models.CharField(max_length=20, blank=True)
	
	def __unicode__(self):
		return self.user.first_name


class Employer(models.Model):
	name		= models.CharField(max_length=50)
	loc			= models.CharField(max_length=50)
	business	= models.CharField(max_length=50, blank=True)
	
	def __unicode__(self):
		return self.name


class Institution(models.Model):
	name		= models.CharField(max_length=50)
	loc			= models.CharField(max_length=50)
	
	def __unicode__(self):
		return self.name

	
class Job(models.Model):
	position	= models.CharField(max_length=50)
	employer	= models.ForeignKey(Employer)
	descr		= models.TextField()
	start_date	= models.DateField()
	end_date	= models.DateField()
	
	def __unicode__(self):
		return self.position


class Education(models.Model):
	title		= models.CharField(max_length=50)
	institution	= models.ForeignKey(Institution)
	descr		= models.TextField(blank=True)
	start_date	= models.DateField()
	end_date	= models.DateField()
	
	def __unicode__(self):
		return self.title


class CV(models.Model):
	author	= models.ForeignKey(Author)
	descr	= models.TextField(blank=True)
	added	= models.DateTimeField(auto_now_add=True)
	updated	= models.DateTimeField(auto_now=True)
	aboutme	= models.TextField(blank=True)
	jobs	= models.ManyToManyField(Job, through='Work')
	edus	= models.ManyToManyField(Education, through='Study')
	
	def __unicode__(self):
		return self.descr


class Work(models.Model):
	cv		= models.ForeignKey(CV)
	job		= models.ForeignKey(Job)
	show	= models.BooleanField(default=True)
	
	def __unicode__(self):
		return self.job.position


class Study(models.Model):
	cv		= models.ForeignKey(CV)
	edu		= models.ForeignKey(Education)
	show	= models.BooleanField(default=True)
	
	def __unicode__(self):
		return self.edu.title
	
	
	