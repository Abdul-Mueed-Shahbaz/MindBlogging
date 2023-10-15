from django.db import transaction
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from ..models import Blog, BlogIP
from .serializers import BlogSerializer
from rest_framework.parsers import MultiPartParser, FormParser

from ...common.constants.app_constants import USER_IP_ADDR
from ...common.constants.filter_constants import CREATED_ON
from ...user.models import UserRelationship


class BlogViewSet(ModelViewSet):
    serializer_class = BlogSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = []
    filter_backends = [SearchFilter]
    search_fields = ['title']

    def get_queryset(self):
        return Blog.objects.all().order_by(CREATED_ON)

    @action(detail=False, methods=['get'], url_path='creator-blogs', url_name='blogs from followed authors',
            permission_classes=[IsAuthenticated])
    def get_blogs_from_followed_authors(self, request):
        user = request.user
        authors = UserRelationship.objects.filter(following_user=user)
        author_ids = authors.values_list('followed_author', flat=True)
        blogs_from_followed_authors = Blog.objects.filter(author__in=author_ids)
        serializer = self.get_serializer(blogs_from_followed_authors, many=True)
        return Response(serializer.data)

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
