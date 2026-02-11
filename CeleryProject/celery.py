import os
from celery import Celery
from time import sleep
from datetime import timedelta
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CeleryProject.settings')

app = Celery('CeleryProject')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

@app.task(name="addition_task")
def subtract(a, b):
    sleep(20)
    return a - b

# # other method
# app.conf.beat_schedule = {
#     'every-8-seconds':{
#         'task':'fishta.tasks.clear_session_cache',
#         'schedule':8,
#         'args':('11111', )
#     }
#     # if want to add the more periodic tasks as needed
# }

# # # other method 
# app.conf.beat_schedule = {
#     'every-9-seconds':{
#         'task':'fishta.tasks.clear_session_cache',
#         'schedule':timedelta(seconds=9),
#         'args':('11111', )
#     }
#     # if want to add the more periodic tasks as needed
# }

# # the method using the timedelta 
app.conf.beat_schedule = {
    'every-9-seconds':{
        'task':'fishta.tasks.clear_session_cache',
        'schedule':crontab(minute='*/1'),
        'args':('11111', )
    }
    # if want to add the more periodic tasks as needed
}