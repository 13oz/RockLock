from django.db import models
from django.contrib import admin

class NewsPost(models.Model):
	title=models.CharField(max_length=75)
	body=models.TextField()
	author=models.CharField(max_length=25)
	datetime=models.DateTimeField(auto_now=True)

	class Meta():
		ordering=['-datetime']

class NewsPostAdmin(admin.ModelAdmin):
	list_display=('title', 'datetime')

admin.site.register(NewsPost, NewsPostAdmin)

# Create your models here.
