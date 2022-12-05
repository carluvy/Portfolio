#!/usr/bin/env bash

# exit on error
set -o errexit

pip3 install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
python manage.py createsuperuser --username=MrsSteele --password=waSteele --email=carngie@gmail.com --noinput