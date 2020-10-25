from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


ADMINS = ('wane', 'wane@hotmail.com')

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'educa',
        'USER': 'educa',
        'PASSWORD': '222',
    }
}
