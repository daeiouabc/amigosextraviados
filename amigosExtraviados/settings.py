"""
Django settings for amigosExtraviados project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kkx7tcw+5pci#y@93blft06%=qd)&7pu93qb(1sm*!@66bc6(p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    #'django.contrib.messages', se desactiva para las notificaciones
    'django.contrib.staticfiles',
    #3
    'rest_framework',

    #'debug_toolbar',  # debug
    'debug_panel',  # debug

    'user_sessions',  # para las notificaciones
    'notifications',  # app para las notificaciones
    'easy_thumbnails',  # app para la creacion de thumbnails
    #
    #'commons',
    'usuario',
    'front',
    'perdido',
    'comentario',
    'geoposition',
    'notificacion',
    'autenticacion'
)

MIDDLEWARE_CLASSES = (
    #'django.contrib.sessions.middleware.SessionMiddleware', se desactiva para las notificaciones
    'debug_panel.middleware.DebugPanelMiddleware',  # debug toolbar
    'user_sessions.middleware.SessionMiddleware',  # para las notificaciones
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'amigosExtraviados.urls'

WSGI_APPLICATION = 'amigosExtraviados.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es-CO'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

#se configura el modelo con el cual se va a tratar la autenticacion
AUTH_USER_MODEL = 'usuario.Usuario'


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}

"""
,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'TEST_REQUEST_RENDERER_CLASSES': (
        'rest_framework.renderers.MultiPartRenderer',
        'rest_framework.renderers.JSONRenderer',
    )
"""
#Geoposition app ettings
GEOPOSITION_MAP_WIDGET_HEIGHT = 400

GEOPOSITION_MAP_OPTIONS = {
    'minZoom': 5,
    'maxZoom': 16,
}

GEOPOSITION_MARKER_OPTIONS = {
    'cursor': 'move'
}
#end geoposition


SESSION_ENGINE = 'user_sessions.backends.db'  # para las notificaciones


#easy tumbnails
THUMBNAIL_ALIASES = {
    '': {
        'mini': {'size': (50, 50), 'crop': True},
        'medio': {'size': (250, 250), 'crop': True},
    },
}

#THUMBNAIL_BASEDIR = 'thum'
THUMBNAIL_EXTENSION = 'jpg'


#mascotas setting
DEFAULT_MASCOTA_IMAGE_SETTING = dict(size=(500, 500), sharpen=True)
