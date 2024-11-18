import os
import pathlib
from decouple import config

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent


POSTGRES_USER = config("POSTGRES_USER", cast=str)
POSTGRES_PASSWORD = config("POSTGRES_PASSWORD", cast=str)
POSTGRES_DB = config("POSTGRES_DB", cast=str)
POSTGRES_HOST = config("POSTGRES_HOST", cast=str)
POSTGRES_PORT = config("POSTGRES_PORT", cast=str)
USE_POSTGRES = config("USE_POSTGRES", cast=bool)

if USE_POSTGRES:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': POSTGRES_DB,
            'USER': POSTGRES_USER,
            'PASSWORD': POSTGRES_PASSWORD,
            'HOST': POSTGRES_HOST,
            'PORT': POSTGRES_PORT,
        }
    }
else:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

