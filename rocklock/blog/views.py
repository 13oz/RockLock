# Create your views here.
from django.template import loader,Context
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django import forms

from rocklock.blog.models import PostContent

class AddPostForm(forms.ModelForm):
	class Meta:
		model = PostContent

def lastPosts(request):
	posts = PostContent.objects.ordered_by('-postDate')[:5]
	template = loader.get_template("main.html")
	cont = Context({'posts': posts})
	return HttpResponse(template.render(cont))

def archive(request):
	posts = PostContent.objects.all
	template = loader.get_template("archive.html")
	cont = Context({'posts': posts})
	return HttpResponse(template.render(cont))

def addPost(request):
	if request.method=='POST':
		form = AddPostForm(request.POST)
		if form.is_valid():
			form.save()
			pass
			return HttpResponseRedirect('')
	else:
		form = AddPostForm()

	return render(request, 'new_post.html', {'form': form})