from sqlalchemy.orm import Session
from user.models.user import User
from user.schemas.user import UserCreate
from fastapi import HTTPException
import traceback

def create_user(db: Session, user: UserCreate) -> User:
    new_user = User(name=user.name, password=user.password, email=user.email, cpf=user.cpf)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
    
def get_all_users(db: Session):
    return db.query(User).all()

def delete_user(db: Session, user_id: int) -> bool:
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return True
    return False
