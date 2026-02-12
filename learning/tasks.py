from celery import shared_task
from time import sleep
from django_celery_beat.models import PeriodicTask, IntervalSchedule
import json
from django.contrib.sessions.models import Session
from django.utils import timezone
from django.core.mail import send_mail
from django.contrib.auth.models import User

@shared_task
def calculate_task(a=5, b=10):
    sleep(5)
    result = (a * 2) + b
    print(f"processing {a} and {b}, result: {result}")
    return result

@shared_task
def factorial_task(n=5):
    sleep(7)
    result = 1
    for i in range(1, n + 1):
        result *= i
    print(f"factorial of {n} is {result}")
    return result

# @shared_task
# def clear_session_cache(id):
#     print(f'session cache is cleared:{id}')
#     return id

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

# # scheduling the periodic task by program
# PeriodicTask.objects.get_or_create(name='factorial-task-every-10-seconds', task='learning.tasks.factorial_task', interval=schedule, args=json.dumps([5]))
# PeriodicTask.objects.get_or_create(name='calculate-task-every-10-seconds', task='learning.tasks.calculate_task', interval=schedule, args=json.dumps([5, 10]))
PeriodicTask.objects.get_or_create(name='Clear RabbitMQ Periodic Task', task='learning.tasks.clear_rabbitmq_data', interval=schedule, args=json.dumps(['hello'])), # passing the arguments to the task as a JSON-encoded list


# email sending task with the console emailbackend

# @shared_task
# def send_email():
#     send_mail(
#         subject = 'testing email from django celery',
#         message = 'this is test email being carried out by celery periodic task',
#         from_email=None,
#         recipient_list=["test@email.com"],
#         fail_silently=False)
    
#     print('email is sent successfully')
#     return 'email sent'


# smtp related task 

@shared_task
def send_email_smtp(subject="hello", message='this is a test email with the SMTP use'):
    recipient_list = list(User.objects.values_list('email', flat=True))

    if recipient_list:
        send_mail(subject=subject, message=message,
            from_email='rehanrural@gmail.com', recipient_list=recipient_list, fail_silently=False)
        print(f'the email is sent {recipient_list}')
        return f'the email sent to {recipient_list}'
    else:
        print('no users found')
        return 'no recipients'

@shared_task
def clear_session_cache():
    count = 0
    
    for session in Session.objects.all():
        if session.expire_date < timezone.now():
            session.delete()
            count += 1
            
    print(f'{count} the expired sessions are cleared')
    return f'{count} sessions are cleared'