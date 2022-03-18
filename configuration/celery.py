from __future__ import absolute_import

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'configuration.settings')

import django
from celery import Celery

from .settings import INSTALLED_APPS

django.setup()

app = Celery('configuration')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(lambda: INSTALLED_APPS)
