from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
from time import sleep
from datetime import timedelta
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_project.settings')

app = Celery('todo_project')
app.conf.enable_utc = False

app.config_from_object(settings, namespace='CELERY')

app.autodiscover_tasks()


app.conf.beat_schedule = {
    'send-reminder-emails-every-hour': {
        'task': 'todo_app.tasks.send_reminder_emails',
        'schedule': crontab(minute=0, hour='*'),  # Every hour
        # 'schedule':crontab(minute='*/1'),  # Every minute
    },
}