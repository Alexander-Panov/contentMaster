from .base import *

DEBUG = True
TEST = True  # Тестовый режим (вместо обращений к openai используются заглушки

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}