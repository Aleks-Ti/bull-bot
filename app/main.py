import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, F, Router, types
from aiogram.enums import Currency, ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from core.utils import (
    MainKeyboard as mk, ReminderKeyboard as rk
)
from dotenv import load_dotenv
from crud.users import create_user, get_user
from crud.reminders import reminder_create as rem_create
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


load_dotenv()

TOKEN = getenv('BOT_TOKEN')

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()


class CycleReminderState(StatesGroup):
    """Машина состояния.

    Ожидание пользовательского.
    """

    description = State()
    cancel = State()


class SingleReminderState(StatesGroup):
    """Машина состояния.

    Ожидание пользовательского.
    """

    description = State()
    cancel = State()


@dp.message(Command("cancel"))
@dp.message((F.text.casefold() == mk.cancel) | (F.text == rk.cancel))
async def cancel_handler(message: types.Message, state: FSMContext) -> None:
    """Обработчик команды отмены."""
    current_state = await state.get_state()
    if current_state is not None:
        logging.info('Cancelling state %r', current_state)
        await state.clear()
        await message.answer('Операция отменена.')
    else:
        await message.answer('Нет активных операций для отмены.')


@dp.callback_query(lambda callback_query: True)
async def handle_callback_query(
    callback_query: types.CallbackQuery, state: FSMContext
):
    """"""
    callback_data = callback_query.data

    if callback_data in rk.__dict__.values():
        CONTROL = 'CONTROL'
        CONTROL = CONTROL
        CONTROL = CONTROL + CONTROL
        await reminder_call_func[callback_data](callback_query, state)
        # await dp.callback_query(callback_query.id)


@dp.message((F.text == mk.off_reminders_today))
async def off_reminders_today(message: types.Message):
    """"""
    print(mk.view_reminders)


@dp.message((F.text == mk.view_reminder_id))
async def view_reminder_id(message: types.Message):
    """"""
    print(mk.view_reminders)


@dp.message((F.text == mk.view_reminders))
async def view_reminders(message: types.Message):
    """"""
    print(mk.view_reminders)


@dp.message((F.text == mk.view_reminders))
async def create_reminder(callback_query: types.CallbackQuery, state=FSMContext):
    """"""
    if rk.cycle_reminder == callback_query.data:
        await state.set_state(CycleReminderState.description)
        await callback_query.message.reply('Введи время')
    else:
        await state.set_state(SingleReminderState.description)
        await callback_query.message.reply('Введите двоичный код 📟 для дешифрации___ ')
    print(mk.view_reminders)


@dp.message(
    (F.text == mk.create_reminders) | (F.text == mk.create_reminders),
)
async def buttons_create_reminders(message: types.Message):
    """"""
    print(mk.create_reminders)
    button_1 = types.InlineKeyboardButton(
        text=rk.cycle_reminder, callback_data=rk.cycle_reminder
    )
    button_2 = types.InlineKeyboardButton(
        text=rk.single_reminder, callback_data=rk.single_reminder
    )
    button_3 = types.InlineKeyboardButton(
        text=rk.cancel, callback_data=rk.cancel
    )
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
                    [button_1], [button_2], [button_3],
                ],
    )
    await message.answer(
        'Какое напоминание хотите создать?',
        reply_markup=keyboard,
    )


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    if message:
        pass

    await create_user(message)
    await get_user(message)

    button_1 = types.KeyboardButton(text=mk.create_reminders)
    button_2 = types.KeyboardButton(text=mk.view_reminders)
    button_3 = types.KeyboardButton(text=mk.view_reminder_id)
    button_4 = types.KeyboardButton(text=mk.off_reminders_today)
    button_5 = types.KeyboardButton(text=mk.cancel)
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[
                    [button_1], [button_2], [button_3], [button_4], [button_5],
                ],
        resize_keyboard=True,
    )

    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(
        f'Привет, {hbold(message.from_user.full_name)}!',
        reply_markup=keyboard,
    )


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == '__main__':
    reminder_call_func = {
        rk.cycle_reminder: create_reminder,
        rk.single_reminder: create_reminder,
        rk.cancel: cancel_handler,
    }
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
