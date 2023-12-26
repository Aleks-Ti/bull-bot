from sqlalchemy import TIMESTAMP, Column, String, Boolean
from datetime import datetime
from app.core.db import Base


class Reminder(Base):
    task_description = Column(String, nullable=True)
    is_completed = Column(Boolean, default=0)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    remind_at = Column(TIMESTAMP, nullable=True)
