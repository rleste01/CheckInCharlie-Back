# crud.py

from sqlalchemy.orm import Session
import models
import schemas
from typing import List

# Import hash_password from security.py instead of auth.py
from security import hash_password

def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    hashed_password = hash_password(user.password)
    db_user = models.User(
        email=user.email,
        hashed_password=hashed_password,
        full_name=user.full_name,
        phone_number=user.phone_number,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str) -> models.User | None:
    return db.query(models.User).filter(models.User.email == email).first()

def update_user(db: Session, db_user: models.User, updates: dict) -> models.User:
    # If 'password' is in updates, handle it by hashing
    if "password" in updates:
        new_plain_password = updates.pop("password")
        if new_plain_password:
            db_user.hashed_password = hash_password(new_plain_password)

    for key, value in updates.items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_all_users(db: Session) -> List[models.User]:
    return db.query(models.User).all()
