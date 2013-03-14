# Create your views here.
from django.template import loader,Context
from django.http import HttpResponse
from rocklock.blog.models import BlogPost

def archive(request):
	posts = BlogPost.objects.all
	template = loader.get_template("archive.html")
	cont = Context({'posts': posts})
	return HttpResponse(template.render(cont))