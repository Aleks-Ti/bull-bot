import os
import redis
from dotenv import load_dotenv
from celery import Celery
load_dotenv()


DATABASE_URL = os.getenv('DATABASE_URL')  # "sqlite:///database.db"

app = Celery('tasks', backend='redis://localhost', broker='pyamqp://')


redis_conn = redis.StrictRedis(host='localhost', port=6379, db=1)
