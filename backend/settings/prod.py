from .base import *

DEBUG = False
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

DATABASES['default'] = {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': env.str('DATABASE_NAME'),
    'USER': env.str('DATABASE_USER'),
    'PASSWORD': env.str('DATABASE_PASSWORD'),
    'HOST': env.str('DATABASE_HOST'),
    'PORT': env.int('DATABASE_PORT', default=5432),
}

# Configuración de seguridad adicional
SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
