from celery import shared_task
from django.contrib.auth.models import User


@shared_task
def multiply_numbers(a, b):
    return a * b


@shared_task(name="new_user", ignore_result=True)
def create_user(username, email, password):
    new_user = User.objects.create_user(username, email, password)
    new_user.save()
