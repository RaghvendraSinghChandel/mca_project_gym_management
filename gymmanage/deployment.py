import os
from .settings import *
from .settings import BASE_DIR

ALLOWED_HOSTS = [os.environ["WEBSITE_HOSTNAME"]]

CRSF_TRUSTED_ORIGINS = ["https;//"+os.environ["WEBSITE_HOSTNAME"]]
DEBUG = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.Middleware.WhiteNoiseMiddleWare',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFiles"

STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'raghvendragym',  # Database name from Azure JSON view
        'USER': 'mobwsugkhg',     # Administrator Login from Azure JSON view
        'PASSWORD': 'Raghvendra1',  # You need to provide the correct password
        'HOST': 'raghvendragym.mysql.database.azure.com',  # Fully Qualified Domain Name from Azure JSON view
        'PORT': '3306',           # Default MySQL port
    }
}
