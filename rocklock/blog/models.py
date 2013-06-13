from django.db import models
from django.contrib import admin

# Create your models here.
class Users(models.Model):
	sex = (
		('M', 'Male'),
		('F', 'Female'),
		)

	login = models.CharField(max_length = 40, unique = True)
	password = models.CharField(max_length = 80) #testing - rtfm django.auth
	firstName = models.CharField(max_length = 25)
	lastName = models.CharField(max_length = 25)
	age = models.IntegerField()
	userSex = models.CharField(max_length = 1, choices = sex)
	
	#TODO - add access rights
	#TODO - подумать над выводом.
	def __unicode__(self):
		return self.login

class Hub(models.Model):
	hubName = models.CharField(max_length = 15, unique = True)
	hubAdmin = models.OneToOneField(Users)

	def __unicode__(self):
		return self.hubName

#TODO add ManyToMany to Post model
class Tag(models.Model):
	tagName = models.CharField(max_length = 20, unique = True)
	postName = #ManyToMany relation

	def __unicode__(self):
		return self.tagName

class PostContent(models.Model):
	postTitle = models.CharField(max_length = 40)
	postText = models.TextField()
	postAuthor = models.CharField(max_length = 40)
	postHub = #OneToMany relation

	def __unicode__(self):
		return self.postTitle