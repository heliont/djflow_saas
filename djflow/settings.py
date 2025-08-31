import sys
import os
from pathlib import Path
from .core.internationalization import *
from .core.applist import *
from .core.json_settings import get_settings
from .core.staticfiles import *
from .core.mediafiles import *
from .core.mailserver import *
from .core.databases import *
from .core.loggin import *

settings = get_settings()

PROJECT_ROOT = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = settings['SECRET_KEY']
DEBUG = settings['DEBUG']
ALLOWED_HOSTS = settings['SECURITY']['ALLOWED_HOSTS']
SECURE_SSL_REDIRECT = settings['SECURITY']['SECURE_SSL_REDIRECT']

DATABASES = settings['DB']

MIDDLEWARE = [
    'tenant_schemas.middleware.TenantMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'djflow.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_ROOT, 'templates')],
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

WSGI_APPLICATION = 'djflow.wsgi.application'
AUTH_PASSWORD_VALIDATORS = settings['AUTH_PASSWORD_VALIDATORS']
LOGIN_URL = '/security/login/'

# Tenants MODEL
TENANT_MODEL = "tenant.Client"