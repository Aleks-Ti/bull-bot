from aiogram import Bot
from aiogram.enums import ParseMode
from dotenv import load_dotenv
from .celery import app
from os import getenv

load_dotenv()

TOKEN = getenv('BOT_TOKEN')


@app.task
def send_reminder(user_id, text):
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    bot.send_message(chat_id=user_id, text=text)
