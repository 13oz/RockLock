# Create your views here.
from django.template import loader,Context
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django import forms

from rocklock.blog.models import PostContent, Hub

class AddPostForm(forms.ModelForm):
	class Meta:
		model = PostContent

def main(request):
	posts = PostContent.objects.order_by('-postDate')[:5]
	hubs = Hub.objects.all
	template = loader.get_template("main.html")
	cont = Context({'posts': posts, 'hubs': hubs})
	return HttpResponse(template.render(cont))

def archive(request):
	posts = PostContent.objects.order_by('-postDate')
	template = loader.get_template("index.html")
	cont = Context({'posts': posts})
	return HttpResponse(template.render(cont))

def addPost(request):
	if request.method=='POST':
		form = AddPostForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
	else:
		form = AddPostForm()

	return render(request, 'new_post.html', {'form': form})

def showPost(request, postID):
	post = PostContent.objects.get(id = postID)
	template = loader.get_template("post.html")
	cont = Context({'post' : post})
	return HttpResponse(template.render(cont))