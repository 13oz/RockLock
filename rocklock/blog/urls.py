from django.conf.urls.defaults import *
import rocklock.blog.views
#from rocklock.blog.views import archive, addPost

urlpatterns = patterns('', 
	url(r'^$', rocklock.blog.views.archive, name="main"),
	url(r'^add_post', rocklock.blog.views.addPost, name="add"),
	url(r'(?P<postID>\d+)/$', rocklock.blog.views.showPost, name="showpost"),)