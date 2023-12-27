import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, F, Router, types
from aiogram.enums import Currency, ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from core.utils import MainKeyboard as mk
from dotenv import load_dotenv
from crud.users import create_user

load_dotenv()

TOKEN = getenv('BOT_TOKEN')

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()


@dp.message(
    (F.text == mk.create_reminds) | (F.text == mk.create_reminds),
)
async def handle_projects(message: types.Message):
    """"""
    print(mk.create_reminds)



@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    if message:
        pass

    await create_user(message)
    # keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton(text=mk.create_reminds)
    button_2 = types.KeyboardButton(text='/view_reminds')
    button_3 = types.KeyboardButton(text='/view_reminds_id')
    button_4 = types.KeyboardButton(text='/off_remind_today')
    button_5 = types.KeyboardButton(text='/Exit')
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[
                    [button_1], [button_2], [button_3], [button_4], [button_5],
                ], resize_keyboard=True,
        )

    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    # create_user(message)
    await message.answer(
        f'Привет, {hbold(message.from_user.full_name)}!', reply_markup=keyboard,
    )


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
