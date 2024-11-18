import os
import pathlib

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent


POSTGRES_USER = str(os.environ.get("POSTGRES_USER"))
POSTGRES_PASSWORD = str(os.environ.get("POSTGRES_PASSWORD"))
POSTGRES_DB = str(os.environ.get("POSTGRES_DB"))
POSTGRES_HOST = str(os.environ.get("POSTGRES_HOST"))
POSTGRES_PORT = str(os.environ.get("POSTGRES_PORT"))
USE_POSTGRES = bool(os.environ.get("USE_POSTGRES"))

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

