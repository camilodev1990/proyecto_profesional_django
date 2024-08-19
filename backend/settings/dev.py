from .base import *

DEBUG = True

DATABASES['default'] = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': BASE_DIR / 'dev_db.sqlite3',
}

# Otras configuraciones específicas de desarrollo
