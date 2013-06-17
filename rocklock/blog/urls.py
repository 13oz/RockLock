from django.conf.urls.defaults import *
from rocklock.blog.views import archive

urlpatterns = patterns('', url(r'^$', archive))