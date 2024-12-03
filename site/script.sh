#!/bin/bash

cd src || { echo "Directory 'src' not found."; exit 1; }

python manage.py migrate

daphne -b 0.0.0.0 -p 8000 config.asgi:application