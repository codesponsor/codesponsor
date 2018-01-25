import os

from django.conf import settings

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'code_sponsor.settings')

app = Celery('code_sponsor')

app.config_from_object('django.conf:settings')

app.conf.update(
    BROKER_URL=settings.CLOUDAMQP_URL,
    CELERY_RESULT_BACKEND=settings.CLOUDAMQP_URL)

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
