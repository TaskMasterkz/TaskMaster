#!/usr/bin/env bash
python manage.py collectstatic --noinput
apt-get update && apt-get install -y graphviz
python manage.py migrate
