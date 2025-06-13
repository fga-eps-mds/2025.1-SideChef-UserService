from sqlalchemy.orm import Session
from user.models.user import User
from user.schemas.user import UserCreate
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from core.security import gerar_hash_senha
import traceback

def create_user(db: Session, user: UserCreate) -> User:
    senha_criptografada = gerar_hash_senha(user.password)
    new_user = User(
        name=user.name,
        password=senha_criptografada,
        email=user.email,
        cpf=user.cpf
    )

    db.add(new_user)
    try:
        db.commit()
        db.refresh(new_user)
        return new_user
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="E-mail ou CPF já cadastrado.")
    
def get_all_users(db: Session):
    return db.query(User).all()

def delete_user(db: Session, user_id: int) -> bool:
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return True
    return False
