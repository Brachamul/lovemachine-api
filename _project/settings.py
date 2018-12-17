import os

######################################################################

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'wb8ua=u$k3cpv*b&#63-@9d!0h)mazegi8-(%xvxg4i1a-5&x'
DEBUG = True
ROOT_URLCONF = '_project.urls'
WSGI_APPLICATION = '_project.wsgi.application'
APPEND_SLASH = True

#--------------------------------------------------------------------

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(PROJECT_ROOT, 'db.sqlite3'),
	}
}

#--------------------------------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join((PROJECT_ROOT), "_static_root")
MEDIA_ROOT = os.path.join((PROJECT_ROOT), "_media_root")
STATICFILES_DIRS = ( os.path.join((PROJECT_ROOT), "static", "static"),)

# Static files : https://docs.djangoproject.com/en/1.9/howto/static-files/

#--------------------------------------------------------------------

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

#--------------------------------------------------------------------

AUTHENTICATION_BACKENDS = [ "django.contrib.auth.backends.ModelBackend", ]

#--------------------------------------------------------------------

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [ os.path.join(PROJECT_ROOT, 'static/templates/'), ],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request', # required for django-allauth
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
			],
		},
	},
]

#--------------------------------------------------------------------

LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Europe/Paris'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Internationalization : https://docs.djangoproject.com/en/1.9/topics/i18n/

######################################################################

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth', # required for allauth
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
]

SITE_ID = 1 # required when using django.contrib.sites

LOGIN_REDIRECT_URL = '/auth/'
LOGIN_URL = '/auth/login/'



######################################################################
# LOCAL APPS
######################################################################

#--------------------------------------------------------------------

# Stores the User model
INSTALLED_APPS += ['users', ]
AUTH_USER_MODEL = 'users.User'


# Stores app data from the Google Play Store
INSTALLED_APPS += ['play_store', ]


# Allows users to rate apps
INSTALLED_APPS += ['ratings', ]


######################################################################
# THIRD-PARTY APPS
######################################################################

#--------------------------------------------------------------------

INSTALLED_APPS += ['rest_framework',] # djangorestframework
# Enables serving a REST API

REST_FRAMEWORK = {
	'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
	'PAGE_SIZE': 100,
}

#--------------------------------------------------------------------

######################################################################

#  Local settings : import local_settings if exist
try: from local_settings import *
except ImportError: pass