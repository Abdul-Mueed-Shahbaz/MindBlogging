from rest_framework.viewsets import ModelViewSet
from ..models import Blog
from .serializers import BlogSerializer
from rest_framework.parsers import MultiPartParser, FormParser


class BlogViewSet(ModelViewSet):
    serializer_class = BlogSerializer
    parser_classes = (MultiPartParser, FormParser)

    def get_queryset(self):
        return Blog.objects.all().order_by('-created_on')
