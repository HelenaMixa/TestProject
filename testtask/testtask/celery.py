import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testtask.settings')
app = Celery('testtask')
app.conf.beat_schedule = {
    'update_data_every_60_seconds': {
        'task': 'orders.tasks.update_data.update_data',
        'schedule': 60.0,
    },
    'update_exchange_value_every_day_on_10_am': {
        'task': 'orders.tasks.update_exchange_value.update_exchange_value',
        'schedule': crontab(hour=10),
    },
    'sent_telegram_messege_on_10_am': {
        'task': 'orders.tasks.send_telegram_messege.sent_telegram_messege',
        'schedule': crontab(hour=10),
    },
}
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
