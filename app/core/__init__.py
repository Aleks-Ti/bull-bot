from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import declarative_base

from app.core.config import settings

Base = declarative_base()

engine = create_async_engine(settings.database_url)