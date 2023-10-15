from django.contrib import admin
from apps.blog.models import Blog, BlogIP

# Register your models here.
admin.site.register(Blog)
admin.site.register(BlogIP)
