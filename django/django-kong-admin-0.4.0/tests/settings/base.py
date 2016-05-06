# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function
import logging
import os
logging.disable(logging.CRITICAL)

import environ
BASE_DIR = environ.Path(os.path.dirname(__file__))

BASE_DIR2 = os.path.dirname(os.path.dirname(__file__))

env = environ.Env(
    KONG_ADMIN_SIMULATOR=(bool, False),
)
SITE_ROOT = BASE_DIR()
DEBUG = True
SECRET_KEY = 'K-pF++*|+9alwjd4834327E;a'

ALLOWED_HOSTS = []
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # https://github.com/DarioGT/django-jsonfield2
    'jsonfield2',

    # https://github.com/bradleyayers/django-ace
    'django_ace',

    'kong_admin'
)
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    # 'django.middleware.csrf.CsrfResponseMiddleware',
)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(str(BASE_DIR), 'templates/'),
            os.path.join(str(BASE_DIR2), 'templates/'),
        ],
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'
#STATIC_URL = os.path.join(BASE_DIR2,'static/')
STATIC_ROOT = os.path.join(BASE_DIR2,'static')
MEDIA_ROOT = os.path.join(BASE_DIR2,'media')
MEDIA_URL = '/media/'
STATICFILES_DIRS = (
   os.path.join(os.path.dirname(BASE_DIR2), 'static/'),
   os.path.join(str(BASE_DIR2), 'templates/model/'),
)
ROOT_URLCONF = 'tests.settings.urls'
