from celery import Celery

from .tasks import *  # noqa

broker_url = 'redis://redis:6379/0'
result_backend = 'rpc://'
include = ['tasks']
app = Celery('tasks', backend=result_backend, broker=broker_url)
