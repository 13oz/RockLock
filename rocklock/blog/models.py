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

class Hub(models.Model):
	hubName = models.CharField(max_length = 15, unique = True)
	hubAdmin = models.OneToOneField(Users)

class Tag(models.Model):
	tagName = models.CharField(max_length = 20, unique = True)

class Post(models.Model): #testing - rtfm relations
	postHub = models.CharField(max_length = 15)
	postTag = models.CharField(max_length = 20)

class PostContent(models.Model):
	postTitle = models.CharField(max_length = 40)
	postText = models.TextField()
	postAuthor = models.CharField(max_length = 40)

"""
class BlogPost(models.Model):
	title = models.CharField(max_length = 150)
	body = models.TextField()
	timestamp = models.DateTimeField()

class BlogPostAdmin(admin.ModelAdmin):
	list_display = ('title', 'timestamp')

admin.site.register(BlogPost, BlogPostAdmin)"""