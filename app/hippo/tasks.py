from celery import shared_task
from celery.utils.log import get_task_logger
from django.contrib.auth.models import User

from hippo.models import Hippo

logger = get_task_logger(__name__)


@shared_task
def multiply_hippo(lst: list):
    logger.info("Multiplying %s by 2" % lst)
    for i in range(len(lst)):
        lst[i] = lst[i] * 2
    return lst

@shared_task
def add(a, b):
    return a + b

@shared_task(name="new_user", ignore_result=True)
def create_hippo(name, color, age):
    new_user = Hippo.objects.create_user(name, color, age)
    new_user.save()
