#!/bin/bash

echo "Starting Application"
python /app/src/manage.py migrate
python /app/src/manage.py runserver 0.0.0.0:8080
python /app/src/manage.py createsuperuser --noinput
echo "The application is ready!"
