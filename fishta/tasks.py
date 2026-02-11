from celery import shared_task
from time import sleep
from django_celery_beat.models import PeriodicTask, IntervalSchedule
import json

@shared_task
def calculate_task(a, b):
    # this is a that multiplies by 2, adds b, then shows a delay and returns result.
    sleep(5) 
    calculation = (a * 2) + b
    print(f"processing {a} and {b}, result: {calculation}")
    return calculation

@shared_task
def factorial_task(n):
    # calculating a factorial of n with a small delay
    sleep(7)
    result = 1
    for i in range(1, n + 1):
        result *= i
    print(f"factorial of {n} is {result}")
    return result

@shared_task
def clear_session_cache(id):
    print(f'session cache is cleared:{id}')
    return id

@shared_task
def clear_redis_data(key):
    print(f'redis data cleared: {key}')
    return key

@shared_task
def clear_rabbitmq_data(key):
    print(f'RabbitMQ data cleared: {key}')
    return key

# creating schedule every 25 seconds
schedule, created = IntervalSchedule.objects.get_or_create(every=25, period=IntervalSchedule.SECONDS)

# scheduling the periodic task by program
PeriodicTask.objects.get_or_create(name='Clear RabbitMQ Periodic Task', task='fishta.tasks.clear_rabbitmq_data', interval=schedule, args=json.dumps(['hello'])), # passing the arguments to the task as a JSON-encoded list
 