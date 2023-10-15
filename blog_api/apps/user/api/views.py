from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from apps.user.api.serializers import RegisterSerializer

User = get_user_model()


class AuthViewSet(GenericViewSet):
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RegisterSerializer
    model = User

    @action(detail=False, methods=['post'], url_path='register', url_name='register a new user')
    def register(self, request):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            response_data = {
                'message': 'User registered successfully',
                'user': {**serializer.data},
            }
            return Response(response_data, status=201)
        return Response(serializer.errors, status=400)

    @action(detail=False, methods=['post'], url_path='login', url_name='login a user')
    def login(self, request):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            response_data = {
                'message': 'User registered successfully',
                'user': {**serializer.data},
            }
            return Response(response_data, status=201)
        return Response(serializer.errors, status=400)
