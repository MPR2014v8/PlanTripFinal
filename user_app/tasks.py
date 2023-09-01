# myapp/tasks.py

from celery import shared_task
from celery.schedules import crontab
from django.core.management import call_command

@shared_task
def add_data_task():
    call_command('add_data')

CELERY_BEAT_SCHEDULE = {
    'add-data-every-5-minutes': {
        'task': 'user_app.tasks.add_data_task',
        'schedule': crontab(minute='*/5'),  # Run every 5 minutes
    },
}
