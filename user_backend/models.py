# models.py

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String, nullable=True)
    phone_number = Column(String, nullable=True)

class Problem(Base):
    __tablename__ = "problems"
    
    id = Column(Integer, primary_key=True, index=True)
    question = Column(String, nullable=False)
    answer = Column(Integer, nullable=False)
    creator_id = Column(Integer, ForeignKey("users.id"))
    recipient_id = Column(Integer, ForeignKey("users.id"))
    time_limit = Column(Integer, nullable=False)  # in seconds
    created_at = Column(DateTime, default=datetime.utcnow)
    solved = Column(Boolean, default=False)
    expires_at = Column(DateTime)