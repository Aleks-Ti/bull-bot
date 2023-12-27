from models import User
from sqlalchemy.ext.asyncio import AsyncSession
from aiogram.types.message import Message
from core.db import AsyncSessionLocal
from sqlalchemy.future import select


async def create_user(data: Message):
    """Создание профиля пользователя если нет в БД."""
    async with AsyncSessionLocal() as session:
        session: AsyncSession
        statement = select(User).filter_by(telegram_id=data.chat.id)
        user_exists = (await session.execute(statement)).scalar() is None

        if user_exists:
            new_user = User(
                username=data.chat.username,
                telegram_id=data.chat.id,
                first_name=data.chat.first_name,
                last_name=data.chat.last_name,
            )

            session.add(new_user)
            await session.commit()
            await session.refresh(new_user)
            return new_user
