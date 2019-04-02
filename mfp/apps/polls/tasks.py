# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task


@shared_task
def add_poll(x, y):
    return x + y


@shared_task
def mul_poll(x, y):
    return x * y


@shared_task
def xsum_poll(numbers):
    return sum(numbers)
