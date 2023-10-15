import jwt
import datetime
from django.conf import settings

from apps.common.constants.app_constants import ACCESS, REFRESH


def create_token(user, expiration, token_type):
    return jwt.encode({
        "email": user.email,
        "username": user.username,
        'type': token_type,
        "exp": datetime.datetime.utcnow() + expiration,
        "iat": datetime.datetime.utcnow()
    }, settings.TOKEN_SECRET, algorithm=settings.ENCODING_ALGORITHM)


def decode_token(token):
    return jwt.decode(token, settings.TOKEN_SECRET, algorithms=[settings.ENCODING_ALGORITHM])


def create_access_token(user):
    return create_token(user=user, expiration=datetime.timedelta(minutes=settings.ACCESS_TOKEN_EXPIRY),
                        token_type=ACCESS)


def create_refresh_token(user):
    return create_token(user=user, expiration=datetime.timedelta(minutes=settings.REFRESH_TOKEN_EXPIRY),
                        token_type=REFRESH)
