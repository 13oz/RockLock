from django.conf.urls.defaults import *
from rocklock.newsline.views import index

urlpatterns = patterns('', url(r'^$', index),)