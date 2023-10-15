from django.db import transaction
from rest_framework.viewsets import ModelViewSet
from ..models import Blog, BlogIP
from .serializers import BlogSerializer
from rest_framework.parsers import MultiPartParser, FormParser

from ...common.constants.app_constants import USER_IP_ADDR
from ...common.constants.filter_constants import CREATED_ON


class BlogViewSet(ModelViewSet):
    serializer_class = BlogSerializer
    parser_classes = (MultiPartParser, FormParser)
    authentication_classes = []

    def get_queryset(self):
        return Blog.objects.all().order_by(CREATED_ON)

    @transaction.atomic
    def retrieve(self, request, *args, **kwargs):
        user_ip = request.META.get(USER_IP_ADDR)
        blog = self.get_object()
        blog_manager_ref = BlogIP.objects

        if not blog_manager_ref.filter(ip_address=user_ip, blog=blog).exists():
            blog_manager_ref.create(ip_address=user_ip, blog=blog)
            blog.views += 1
            blog.save()

        return super().retrieve(request, *args, **kwargs)
