import os

from django.conf import settings

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'code_sponsor.settings')

app = Celery('code_sponsor')

app.config_from_object('django.conf:settings')

app.conf.update(
    BROKER_URL=os.environ['CLOUDAMQP_URL'],
    CELERY_RESULT_BACKEND=os.environ['CLOUDAMQP_URL'])

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
