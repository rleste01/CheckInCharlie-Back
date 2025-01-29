# schemas.py

from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None
    phone_number: Optional[str] = None

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int

    class Config:
        # For Pydantic v2, the new key is `from_attributes`
        # This allows Pydantic to convert SQLAlchemy objects -> Pydantic models
        from_attributes = True

class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    phone_number: Optional[str] = None
    password: Optional[str] = None

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

class ProblemCreate(BaseModel):
    question: str
    answer: int
    recipient_id: int
    time_limit: int

class ProblemOut(BaseModel):
    id: int
    question: str
    creator_id: int
    recipient_id: int
    time_limit: int
    created_at: datetime
    solved: bool
    
    class Config:
        from_attributes = True