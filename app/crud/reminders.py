from models import Reminder, UserReminder
from sqlalchemy.ext.asyncio import AsyncSession
from aiogram.types.message import Message
from core.db import AsyncSessionLocal
from crud.users import get_user


async def reminder_create(data: Message, *_):
    """Создание профиля пользователя если нет в БД."""
    async with AsyncSessionLocal() as session:
        session: AsyncSession

        user_db = get_user(data)

        if user_db is not None:
            new_reminder = Reminder(
                task_description=data.chat.username,
                is_completed=0,
            )
            relation = UserReminder(
                users_id=user_db.id,
                reminder_id=data.chat.id
            )

            session.add(new_reminder)
            session.add(relation)
            await session.commit()
            await session.refresh(new_reminder)
            await session.refresh(relation)
