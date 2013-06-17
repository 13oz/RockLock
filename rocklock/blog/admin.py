from django.contrib import admin
from rocklock.blog.models import PostContent, Hub, Users

admin.site.register(PostContent)
admin.site.register(Hub)
admin.site.register(Users)