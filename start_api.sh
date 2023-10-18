#!/bin/bash
set -x;

sleep 5

python manage.py create_kafka_topics

python manage.py makemigrations

python manage.py migrate

python manage.py create_users

python manage.py first_consumer &

python manage.py second_consumer &

python manage.py runserver 0.0.0.0:8000

trap : TERM INT; sleep infinity & wait