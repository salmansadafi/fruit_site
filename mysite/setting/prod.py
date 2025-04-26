from mysite.settings import *
import os
import dj_database_url

DEBUG =  False

DATABASES = {
    'default': dj_database_url.config(default='sqlite:///dummy.db')
}
SITE_ID = 2

ALLOWED_HOSTS = ['https://fruit.liara.run','fruit.liara.run','www.fruit.liara.run']

STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_ROOT = BASE_DIR / 'media'
COMPRESS_ROOT = STATIC_ROOT

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # یا mailgun, sendgrid و غیره
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'sadafitehran.ms@gmail.com'
EMAIL_HOST_PASSWORD = 'ncyj cjhj qzzt cqny'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
]


STATICFILES_FINDERS += ['compressor.finders.CompressorFinder']
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True