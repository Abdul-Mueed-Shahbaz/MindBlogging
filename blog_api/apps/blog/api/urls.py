# from django.urls import path
from rest_framework import routers

from apps.blog.api.views import BlogViewSet

router = routers.DefaultRouter()
router.register(r'blogs', BlogViewSet, basename='blogs')

urlpatterns = [
                  # path(''),
              ] + router.urls
