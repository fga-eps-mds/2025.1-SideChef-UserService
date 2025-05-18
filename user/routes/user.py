
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from user.schemas import UserCreate
from user.models import User
from core.database import get_db


router = APIRouter()

@router.post("/", status_code=201)

def create_user(user: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email já cadastrado.")

    new_user = User(
        name=user.name,
        email=user.email,
        password=user.password  # SEM criptografia por enquanto
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"id": new_user.id, "name": new_user.name, "email": new_user.email}

