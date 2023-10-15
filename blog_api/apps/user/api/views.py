from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.user.api.serializers import RegisterSerializer, AuthTokenObtainPairSerializer

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


class AuthTokenObtainPairView(TokenObtainPairView):
    serializer_class = AuthTokenObtainPairSerializer

    # Override the post method to add additional validation
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
