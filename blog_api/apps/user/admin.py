from django.contrib import admin
from apps.user.models import User, UserRelationship

# Register your models here.
admin.site.register(User)
admin.site.register(UserRelationship)
