# Create your views here.
from django.template import loader,Context
from django.http import HttpResponse
from rocklock.newsline.models import NewsPost

def index(request):
	newsline=NewsPost.objects.all
	template = loader.get_template("index.html")
	cont = Context({'newsline': newsline})
	return HttpResponse(template.render(cont))