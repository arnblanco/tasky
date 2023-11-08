import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from pathlib import Path

# load .env
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# PROJECT NAME
PROJECT_NAME = 'PROJECT_NAME' in os.environ and os.environ['PROJECT_NAME'] or ''
MAX_UPLOAD_SIZE = "5242880"

SUMMERNOTE_CONFIG = {
    'disable_attachment': True,
}
X_FRAME_OPTIONS = 'ALLOWALL'
XS_SHARING_ALLOWED_METHODS = ['POST','GET','OPTIONS', 'PUT', 'DELETE']

# #############################################################################
# SECURITY WARNING
# #############################################################################
SECRET_KEY = 'SECRET_KEY' in os.environ and os.environ['SECRET_KEY'] or ''

# #############################################################################
# EMAIL CONFIG AND BACKEND
# #############################################################################
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_SSL = True
EMAIL_HOST = 'EMAIL_HOST' in os.environ and os.environ['EMAIL_HOST'] or ''
EMAIL_HOST_USER = 'EMAIL_HOST_USER' in os.environ and os.environ['EMAIL_HOST_USER'] or ''
EMAIL_HOST_PASSWORD = 'EMAIL_HOST_PASSWORD' in os.environ and os.environ['EMAIL_HOST_PASSWORD'] or ''
EMAIL_PORT = 'EMAIL_PORT' in os.environ and os.environ['EMAIL_PORT'] or ''

# #############################################################################
# AWS KEYS CONFIG
# #############################################################################
AWS_ACCESS_KEY_ID = 'AWS_ACCESS_KEY_ID' in os.environ and os.environ['AWS_ACCESS_KEY_ID'] or ''
AWS_SECRET_ACCESS_KEY = 'AWS_SECRET_KEY' in os.environ and os.environ['AWS_SECRET_KEY'] or ''

# #############################################################################
# KEYS FOR SOCIAL AUTH
# #############################################################################
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'SOCIAL_AUTH_GOOGLE_OAUTH2_KEY' in os.environ and os.environ['SOCIAL_AUTH_GOOGLE_OAUTH2_KEY'] or ''
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET' in os.environ and os.environ['SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET'] or ''

# Debug and Host Configurations
DEBUG = True
ALLOWED_HOSTS = ['localhost', 'localhost:8000']


# Application definition
INSTALLED_APPS = [
    #APP's Nativas
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',

    #APP's Liberiras adicionales

    #APP's Propias
    '_apps.website',
    '_apps.tareas',
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

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / '_templates'],
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

ROOT_URLCONF = 'core.urls'
WSGI_APPLICATION = 'core.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

#Auth Login options
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/'

#Authentications Backends
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.RemoteUserBackend',
    'django.contrib.auth.backends.ModelBackend',
]

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'SQL_DATABASE' in os.environ and os.environ['SQL_DATABASE'] or '',
        'USER': 'SQL_USER' in os.environ and os.environ['SQL_USER'] or '',
        'PASSWORD': 'SQL_PASSWORD' in os.environ and os.environ['SQL_PASSWORD'] or '',
        'HOST': 'SQL_HOST' in os.environ and os.environ['SQL_HOST'] or '',
        'PORT': 'SQL_PORT' in os.environ and os.environ['SQL_PORT'] or '',
        'OPTIONS': {
            'options': '-c search_path=public'
        },
    }        
}

# Internationalization
LANGUAGE_CODE = 'es-mx'
TIME_ZONE = 'America/Mexico_City'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / '_collectstatic'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
STATICFILES_DIRS = [
    BASE_DIR / '_statics'
]

# #############################################################################
# AWS S3 STORAGE
# #############################################################################
AWS_SES_REGION_NAME = 'us-west-2'
AWS_STORAGE_BUCKET_NAME = PROJECT_NAME
BOTO_S3_BUCKET = AWS_STORAGE_BUCKET_NAME
AWS_DEFAULT_ACL = 'public-read'
AWS_S3_SECURE_URLS = True
AWS_QUERYSTRING_AUTH = False

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

future = datetime.now() + timedelta(days=10)
AWS_HEADERS = {
    'Expires': future.strftime('%a, %d %b %Y %H:%M:%S GMT'),
    'Cache-Control': 'max-age=86400, public'
}

# #############################################################################
# MEDIA & STATIC & TEMPLATES
# #############################################################################
MEDIA_URL = 'http://s3-%s.amazonaws.com/%s/' % (AWS_SES_REGION_NAME, AWS_STORAGE_BUCKET_NAME)

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
