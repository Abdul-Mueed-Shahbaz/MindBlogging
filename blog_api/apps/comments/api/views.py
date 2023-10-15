from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import CommentsSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser, FormParser
from apps.comments.models import Comments
from apps.common.utils.auth import JwtAuthentication


class CommentsViewSet(ModelViewSet):
    serializer_class = CommentsSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Comments.objects.all().order_by('-created_on')
