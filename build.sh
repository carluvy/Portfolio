#!/usr/bin/env bash

# exit on error
set -o errexit

pip3 install --upgrade pip
pip3 install -r requirements.txt
#pip3 install upgrade --all


python manage.py collectstatic --no-input
python manage.py migrate
#python manage.py createsuperuser --username=admin  --no-input