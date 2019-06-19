"""
Django settings for seo project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import datetime,random

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z&y0=8)b&9h4tvh+$=#0l&8kxy%5p%@jmxc_#57h8nh$02=y2d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'seo_app',
    'django_filters',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'seo_app.middleware.ResponseMiddleware'
]

ROOT_URLCONF = 'seo.urls'

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

WSGI_APPLICATION = 'seo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME':'seo',
    'USER': 'seo',
    'PASSWORD': 'seo@orderplus.com',
    'HOST': '127.0.0.1',
    'PORT': '3307',
    'OPTIONS': {"init_command": "SET foreign_key_checks = 0;",}
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

AUTH_USER_MODEL = "seo_app.User"

APPEND_SLASH = False


list_str = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 's', 't', 'x', 'y',
            'z']

JWT_AUTH_HEADER_PREFIX = "".join(random.sample(list_str, 4))

JWT_AUTH = {
    'JWT_AUTH_HEADER_PREFIX': JWT_AUTH_HEADER_PREFIX,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7),
    'JWT_SECRET_KEY': 'seo',
}


#######################
# DEFINE EMAIL CONFIG #
#######################

EMAIL_HOST = "smtpout.secureserver.net"
EMAIL_PORT = 465
EMAIL_HOST_USER = "service@pinbooster.seamarketings.com"
EMAIL_HOST_PASSWORD = "orderplus"
DEFAULT_FROM_EMAIL = "PinBooster Customer Support <service@pinbooster.seamarketings.com>"
EMAIL_USE_SSL = True
EMAIL_SUBJECT_PREFIX = " "
# 默认邮件接收方(开发人员，如果代码出现极端异常可进行邮件通知.)
DEFAULT_TO_EMAILS = ["877252373@qq.com", ]