from celery.utils.log import get_task_logger
from django.apps import apps

from configuration.celery import app

logger = get_task_logger(__name__)


@app.task
def count_teachers():
    model = apps.get_model(app_label='authentication', model_name='User')
    logger.info(f'{model.objects.filter(is_staff=True).count()}')
