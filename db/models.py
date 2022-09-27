from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from .database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(150))
    description = Column(String, nullable=True)
    timestamp = Column(DateTime(timezone=True), default=datetime.now)
