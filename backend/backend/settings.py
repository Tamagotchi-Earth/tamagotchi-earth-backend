import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-15blib&w2rj4=wuhv*@p#05)307b@!uoan98=9da7q&3s9&fup'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.environ.get('DJANGO_DEBUG', True))

ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', default='*').split(" ")
if '*' not in ALLOWED_HOSTS and (_domain_name := os.environ.get('NGINX_DOMAIN_NAME')) is not None:
    ALLOWED_HOSTS.append(_domain_name)

# Application definition
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles'
]

EXTERNAL_APPS = [
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django_cleanup',
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'drf_spectacular',
    'rest_framework',
    'modeltranslation'
]

INTERNAL_APPS = [
    'apps.products',
    'apps.users'
]

INSTALLED_APPS = EXTERNAL_APPS + DJANGO_APPS + INTERNAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'common.middleware.DisableAdminI18nMiddleware'
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'backend.wsgi.application'

# List of availible databases for project (sqlite for development, postgres for deployment inside Docker)
AVAILIBLE_DATABASES = {
    'sqlite': {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    },
    'postgres': {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'postgres',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': 'db',
            'PORT': 5432
        }
    }
}

# Selected database
DATABASES = AVAILIBLE_DATABASES[os.environ.get('DJANGO_DB_TYPE', 'sqlite')]

# Password validation
AUTH_PASSWORD_VALIDATORS = []
if not DEBUG:
    # Disable password validation for debug mode
    AUTH_PASSWORD_VALIDATORS += [
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

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'api/static/'
STATIC_ROOT = BASE_DIR / 'static'

# Media files
MEDIA_URL = 'api/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Logging configuration
LOG_DIRECTORY = BASE_DIR / 'logs'
LOGGING = {
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {name} : {message}',
            'style': '{',
        }
    },
    'handlers': {
        'file_apps': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': LOG_DIRECTORY / 'apps.log',
            'formatter': 'verbose'
        },
        'file_django': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': LOG_DIRECTORY / 'django.log',
            'formatter': 'verbose'
        },
        'console': {
            'level': 'DEBUG' if DEBUG else 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'apps': {
            'handlers': ['file_apps', 'console'],
            'level': 'DEBUG',
        },
        'django': {
            'handlers': ['file_django', 'console'],
            'level': 'INFO',
            'propagate': False
        },
        'django.utils.autoreload': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False
        }
    }
}

# Custom user model
AUTH_USER_MODEL = 'users.CustomUser'

# Django REST Framework settings
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'common.openapi.CustomAutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication'
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ]
}
if DEBUG:
    # Add basic auth for OpenAPI convenience
    REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'] += [
        'rest_framework.authentication.BasicAuthentication'
    ]

# dj-rest-auth settings
REST_USE_JWT = True
REST_AUTH_TOKEN_MODEL = None
REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'apps.users.serializers.CustomUserDetailsSerializer'
}
REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'apps.users.serializers.CustomRegisterSerializer'
}

# allauth settings
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_UNIQUE_EMAIL = True

# OpenAPI settings
SPECTACULAR_SETTINGS = {
    'TITLE': 'Tamagotchi earth backend API',
    'VERSION': '1.0.0',
    'SCHEMA_PATH_PREFIX': '/api',
    'COMPONENT_SPLIT_REQUEST': True  # To fix JWT token serializers
}

# Modeltranslation settings
LANGUAGES = [
    ('en', "English"),
    ('ru', "Russian")
]
