from ..models import Blog
from .serializers import BlogSerializer
from rest_framework import permissions, viewsets
from rest_framework.parsers import MultiPartParser, FormParser

from ...common.utils.auth import JwtAuthentication


class MyModelViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.order_by('created_on')
    serializer_class = BlogSerializer
    parser_classes = (MultiPartParser, FormParser)
    authentication_classes = JwtAuthentication
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
