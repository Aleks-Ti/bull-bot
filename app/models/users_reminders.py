from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from core.db import Base


class UserReminder(Base):
    users_id = Column(UUID, ForeignKey(
        'user.id', ondelete='CASCADE'), primary_key=True,
    )
    reminder_id = Column(UUID, ForeignKey(
        'reminder.id', ondelete='CASCADE'), primary_key=True,
    )
