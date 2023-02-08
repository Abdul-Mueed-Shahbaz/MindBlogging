from .base import *

DEBUG = False

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # i.e
        # 'NAME': 'blog-api',
        # 'USER': 'root',
        # 'PASSWORD': 'root',
        # 'HOST': '127.0.0.1',
        # 'PORT': '3306',
    }
}

CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOWED_ORIGINS = [
    # i.e "http://127.0.0.1:9000",
]
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = [
    # i.e 'ACCESS_TOKEN'
]

