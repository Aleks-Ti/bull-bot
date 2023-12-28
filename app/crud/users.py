from models import User
from sqlalchemy.ext.asyncio import AsyncSession
from aiogram.types.message import Message
from core.db import AsyncSessionLocal
from sqlalchemy.future import select


async def exists_user(data: Message) -> bool:
    """Проверяет, существует ли пользователь в базе данных."""

    async with AsyncSessionLocal() as session:
        session: AsyncSession
        statement = select(User).filter_by(telegram_id=data.chat.id)
        user_exists = (await session.execute(statement)).scalar() is None
        return user_exists


async def get_user(data: Message) -> User | None:
    """Возвращает данные о юзере из БД."""

    async with AsyncSessionLocal() as session:
        session: AsyncSession
        statement = select(User).filter_by(telegram_id=data.chat.id)
        user = (await session.execute(statement)).scalar()
        return user


async def create_user(data: Message) -> None:
    """Создание пользователя в БД."""

    user_exists = await exists_user(data)

    if user_exists:
        async with AsyncSessionLocal() as session:
            session: AsyncSession
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
