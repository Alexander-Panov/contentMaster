import os

from .base import *

DEBUG = False

ADMINS = [
    ('Alexander', 'palehou@gmail.com'),
]

ALLOWED_HOSTS = [f".{os.environ.get('DOMAIN')}"]  # mysite.com и любой поддомен *.mysite.com

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': 5432,
    }
}

# Безопасность
# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True
# SECURE_SSL_REDIRECT = True
