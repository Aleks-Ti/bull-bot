import asyncio
import logging
import sys
from os import getenv
from strenum import StrEnum
from aiogram import Bot, Dispatcher, F, Router, types
from aiogram.enums import Currency, ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from db.query.create_user import create_user
from dotenv import load_dotenv

load_dotenv()

# Bot token can be obtained via https://t.me/BotFather
TOKEN = getenv('BOT_TOKEN')

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()


class MainKeyboardMessages(StrEnum):
    projects: str = 'Проект'



@dp.message(
    (F.text == '/projects') | (F.text == MainKeyboardMessages.projects),
)
async def handle_projects(message: types.Message):
    """Это рабочее, ловит Проект и /projects."""
    print('asdasdas')


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    if message:
        pass
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    create_user(message)

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton(text=MainKeyboardMessages.pr)
    button_2 = types.KeyboardButton(text=CONVERT_BINARY_CODE_IN_WORD)
    button_3 = types.KeyboardButton(text=GAMES_GUESS_NUMBER)
    button_4 = types.KeyboardButton(text=ME_PROFILE)
    button_5 = types.KeyboardButton(text='/Exit')
    keyboard.add(button_1, button_2, button_3, button_4, button_5)
    await message.answer(f'Hello, {hbold(message.from_user.full_name)}!')


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
