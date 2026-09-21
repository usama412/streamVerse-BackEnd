#!/bin/sh
set -e
python manage.py makemigrations accounts catalog library billing blog notifications analytics
python manage.py migrate
python manage.py seed_streamverse
exec "$@"
