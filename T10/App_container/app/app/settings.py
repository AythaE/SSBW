# -*- coding: utf-8 -*-
"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 1.10.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2q+90tq9c@hi=(+10r%!n%ae-l97m8e@exw_cs_^m!4v0nig%u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_mongoengine',
    'restaurantes',     # Añadir nuestra aplicacion
    'registration',
    'bootstrap4',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}

# If True, the user will be automatically logged in.
REGISTRATION_AUTO_LOGIN = True
# The page you want users to arrive at after they successful log in
LOGIN_REDIRECT_URL = '/restaurantes/'
# The page users are directed to if they are not logged in,
LOGIN_URL = '/accounts/login/'
# and are trying to access pages requiring authentication


ROOT_URLCONF = 'app.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

# Dejaremos esta base de datos para usuarios y cosas internas de Django
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

# Comentado el contenido para eliminar validadores de contraseña y poder
# poner contraseñas "fáciles"
AUTH_PASSWORD_VALIDATORS = [

    # {
    #         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    #     },
    #         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    #     {
    #     },
    #     {
    #         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    #     },
    #     {
    #         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    #     },

]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

STATIC_ROOT = 'static'

LOG_FILE = 'restaurantes.log'

LOGGING = {
    'version': 1,

    'disable_existing_loggers': False,

    'formatters': {

        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },

        'simple': {
            'format': '%(levelname)s [%(name)s:%(lineno)s] %(message)s'
        },
    },

    'handlers': {

        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, LOG_FILE),
            'formatter': 'verbose',
            'mode': 'w'
        },

        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },

    'loggers': {
        'django': {
            'handlers': ['file'],
            'propagate': True,
            'level': 'ERROR',
        },

        'restaurantes': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
        },
    }
}
