web: NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program gunicorn code_sponsor.wsgi --log-file -
worker: NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program celery -A code_sponsor worker -l info
release: python manage.py migrate