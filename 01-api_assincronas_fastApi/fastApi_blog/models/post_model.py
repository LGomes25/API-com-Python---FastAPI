from sqlalchemy import Column, Integer, String, Boolean, DateTime
from ..database import Base
import datetime

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    published_at = Column(DateTime, default=datetime.datetime.utcnow)
    published = Column(Boolean, default=False)
    author = Column(String, nullable=False)
