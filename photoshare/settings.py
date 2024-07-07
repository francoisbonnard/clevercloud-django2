
from pathlib import Path
from decouple import config

import pymysql
pymysql.install_as_MySQLdb()

import os

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG',cast=bool)
print("____________debug")
print(DEBUG)

ALLOWED_HOSTS = ['10.2.190.195','10.2.140.21','127.0.0.1','pelimelo.cleverapps.io']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'photo.apps.PhotoConfig',
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

ROOT_URLCONF = 'photoshare.urls'

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

WSGI_APPLICATION = 'photoshare.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

if  config('DEBUG',cast=bool) == True:
    DATABASES = {
        "default": {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
    }
}
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            # 'MYSQL_ADDON_HOST':config('MYSQL_ADDON_HOST'),
            # 'MYSQL_ADDON_DB':config('MYSQL_ADDON_DB'),
            # 'MYSQL_ADDON_USER':config('MYSQL_ADDON_USER'),
            # 'MYSQL_ADDON_PORT':config('MYSQL_ADDON_PORT',cast=int),
            # 'MYSQL_ADDON_PASSWORD':config('MYSQL_ADDON_PASSWORD'),
            # 'MYSQL_ADDON_URI':config('MYSQL_ADDON_URI')
            'NAME': config('MYSQL_ADDON_DB'),
            'USER': config('MYSQL_ADDON_USER'),
            'PASSWORD': config('MYSQL_ADDON_PASSWORD'),
            'HOST': config('MYSQL_ADDON_HOST'),
            'PORT': config('MYSQL_ADDON_PORT',cast=int),
    }
}



print("user db")
print(config('MYSQL_ADDON_USER'))

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

# STATIC_URL = '/static/'
STATIC_URL = config('STATIC_URL_PREFIX',default='/static/')

# Add these new lines
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
print("debug static")
print(STATIC_ROOT)
print(STATIC_URL)
print(STATICFILES_DIRS)

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'





