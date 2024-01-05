import os
# import redis
from dotenv import load_dotenv

load_dotenv()


DATABASE_URL = os.getenv('DATABASE_URL')  # "sqlite:///database.db"

# redis_conn = redis.StrictRedis(host='localhost', port=6379, db=1)
