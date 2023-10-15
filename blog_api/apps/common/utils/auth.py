import jwt.exceptions
from rest_framework import authentication
from rest_framework.authentication import get_authorization_header
from rest_framework.exceptions import AuthenticationFailed
from apps.common.constants.app_constants import INVALID_TOKEN_TYPE, UNAUTHORIZED
from apps.common.utils.utils import decode_token
from apps.user.models import User


class JwtAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        # token = request.COOKIES.get('auth_token') or request.META.get('HTTP_AUTHTOKEN')
        token = get_authorization_header(request)
        # Header name should be Authorization and the value should be Bearer {Token value}

        if not token:
            return None

        token = token.split()[1]
        try:
            payload = decode_token(token)
            token_type = payload['type']
            if not token_type == 'access':
                raise AuthenticationFailed(INVALID_TOKEN_TYPE)
            user = User.objects.filter(email=payload['email']).first()
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed(UNAUTHORIZED)

        return user, None  # authentication successful
