from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView

from apps.user.api.serializers import RegisterSerializer
from apps.user.models import User


class RegisterUser(CreateAPIView):
    model = User
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RegisterSerializer
