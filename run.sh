#!/bin/bash

echo "Migrating database..."

python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

echo "Creating superuser..."

DJANGO_SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL}
DJANGO_SUPERUSER_USERNAME=${DJANGO_SUPERUSER_USERNAME}
DJANGO_SUPERUSER_PASSWORD=${DJANGO_SUPERUSER_PASSWORD}

python3 manage.py createsuperuser \
    --email $DJANGO_SUPERUSER_EMAIL \
    --username $DJANGO_SUPERUSER_USERNAME \
    --noinput || true

echo "Collecting static files..."

python3 manage.py collectstatic --noinput

gunicorn backend.wsgi:application --bind 0.0.0.0:8000 --workers 3
