import environ
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Configuración de environ
env = environ.Env()
environ.Env.read_env()

# Seguridad
SECRET_KEY = env.str('SECRET_KEY')

# modo desarrollo - produccion 
DEBUG = env.bool('DEBUG', default=False)

#host a los que se puede acceder 
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default='localhost')


# Aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
]


# Middleware #tienen caracteristicas de seguridad, gestion de sesiones, autenticacion y proteccion crsf y clickjacking
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]



# Configuración de plantillas
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'frontend' / 'templates',
        ], #aqui se escriben directorios de templates que esten fuera de las apps
        'APP_DIRS': True, #da orden de buscar plantillas dentro de carpetas templates de las apps
        'OPTIONS': {
            'context_processors': [ #es una lista de funciones que inyectan variables adicionales en el contexto de todas las plantillas.
                'django.template.context_processors.debug',#proporciona informacion de depuracion al contexto, util si tienes debug=true, variables como sql_queries una lista de todas las consultas sql realizadas
                'django.template.context_processors.request', #incluye el objeto request en la plantilla para acceder a request.user o request.path
                'django.contrib.auth.context_processors.auth', #representa al usuario actual autenticado (o AnonymousUser si no hay un usuario autenticado). También añade perms, que proporciona una interfaz para verificar permisos de usuario en las plantillas.
                'django.contrib.messages.context_processors.messages', #añade el framework de django al contexto, permite mostrar mensajes de exito o error
            ],
        },
    },
]



# Configuración de la base de datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / env.str('DATABASE_NAME'),
    }
}

# Validadores de contraseñas 
#lista de validadores que garantizan contraseñas seguras, longitud adecuada, y requisitos de seguridad
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internacionalización  
LANGUAGE_CODE = 'es' #lenguaje
TIME_ZONE = 'America/Bogota' #zona horaria
USE_I18N = True #permite traducir textos del proyecto a diferentes idiomas
USE_TZ = True 
#indica si django va a usar zona horaria en sus operaciones
#en True django almacena tiempos en UTC en la db y los convertira en zona horaria local para mostrarlos


# Configuración de correo electrónico
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env.str('EMAIL_HOST')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env.str('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env.str('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = env.str('EMAIL_HOST_USER')
DEFAULT_SUPPORT_EMAIL = env.str('EMAIL_HOST_USER')


#punto de entrada de la app WSGI de django.
#utilizado para desplegar el proyecto en servidores que soportan WSGI, como Gunicorn o uWSGI
#¿Cómo se configura?
#Normalmente, no es necesario cambiar esta configuración. 
#Apunta a backend.wsgi.application, lo cual es correcto 
#si tu proyecto se llama backend y sigues la estructura estándar de Django.
WSGI_APPLICATION = 'backend.wsgi.application'


#punto de entrada para la app ASGI de django.
#se usa para manejar solicitudes asincronas y trabajar con websockets entre otros.
#se configura igual que wsgi
ASGI_APPLICATION = 'backend.asgi.application'


#define el archivo de configuración de URL principal de tu proyecto Django. 
#Django utilizará este archivo para encontrar las rutas (URLs) que definen 
#las vistas y las funciones de tu aplicación.
#¿Cómo se configura?
#El valor típico es 'backend.urls', que apunta al archivo urls.py 
#dentro de tu proyecto, si tu proyecto se llama backend.
ROOT_URLCONF = 'backend.urls'


# Archivos estáticos - nombre de la carpeta donde va a buscar los estaticos
STATIC_URL = '/static/'


# carpeta de estaticos fuera de las aplicaciones - la llame static
STATICFILES_DIRS = [
    BASE_DIR / 'frontend' / 'static',
]

# nombre de carpeta donde se guardaran los estaticos cuando vaya a produccion con el comando collestatic
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') 

# nombre de la carpeta donde se buscara los archivos multimedia que yo utilizo para el proyecto
MEDIA_URL = '/media/'


# Archivos multimedia - aqui se guardan los archivos subidos por los usuarios en la web
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')




# Campo de clave primaria por defecto
#BigAutofield es un entero grande que se utiliza para guardar claves primarias
#para proyectos con alto flujo de usuarios
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'




# Redirección por defecto al iniciar sesión 
# especifica la URL a la que se redirige a un usuario después de que inicia sesión con éxito.
LOGIN_REDIRECT_URL = '/'