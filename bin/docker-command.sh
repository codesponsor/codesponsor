#!/bin/bash
pipenv run python manage.py createcachetable
pipenv run manage.py collectstatic --noinput -i other
pipenv run manage.py migrate
pipenv run manage.py runserver 0.0.0.0:8000