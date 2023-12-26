from sqlalchemy import ForeignKey, Column, Integer
from datetime import datetime
from app.core.db import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID
import uuid


class UserReminder(Base):
    users_id = Column(UUID, ForeignKey(
        'user.id', ondelete='CASCADE'), primary_key=True
    )
    reminder_id = Column(UUID, ForeignKey(
        'reminder.id', ondelete='CASCADE'), primary_key=True
    )
