from datetime import datetime

from sqlalchemy import TIMESTAMP, Column, Integer, String

from core.db import Base


class User(Base):
    username = Column(String)
    telegram_id = Column(Integer, unique=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    last_channel_visit = Column(TIMESTAMP, default=datetime.utcnow)
