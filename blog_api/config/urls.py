from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

api_prefix = 'api/v1/'

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path(api_prefix, include('apps.blog.api.urls')),
                  path(api_prefix, include('apps.comments.api.urls')),
                  path(api_prefix, include('apps.user.api.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
