#!/bin/sh
set -e

if [ "$RUN_MODE" = "web" ]; then
  python manage.py makemigrations --no-input
  python manage.py migrate --no-input
  python manage.py createadmin
fi

exec "$@"
