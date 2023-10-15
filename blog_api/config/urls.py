from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from apps.blog.api.views import BlogViewSet
from apps.comments.api.views import CommentsViewSet

api_prefix = 'api/v1/'
router = DefaultRouter()

router.register(api_prefix + r'blogs', BlogViewSet, basename='blogs')
router.register(api_prefix + r'comments', CommentsViewSet, basename='comments')

urlpatterns = [
    path(api_prefix + 'admin/', admin.site.urls),
    path(api_prefix, include('apps.user.api.urls')),
]

urlpatterns += router.urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
