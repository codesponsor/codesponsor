#!/bin/sh
set -e

while ! pg_isready -h "$POSTGRES_HOST" -p "$POSTGRES_PORT"; do
    >&2 echo "Postgres is unavailable! Waiting..."
    sleep 1
done

>&2 echo "Postgres is up!"

python3 manage.py collectstatic --noinput
python3 manage.py migrate --noinput

exec "$@"
