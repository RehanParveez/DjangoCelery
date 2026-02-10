from celery import shared_task
from time import sleep

@shared_task
def subtract(a, b):
    sleep(20)
    return a - b

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

