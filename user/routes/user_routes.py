from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from user.schemas.user import UserCreate, UserOut

from user.services.user_functions import create_user

from core.database import get_db

from user.services.user_functions import create_user, get_all_users 
from typing import List

router = APIRouter()

@router.post("/", response_model=UserOut, status_code=201)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.get("/", response_model=List[UserOut])
def list_users(db: Session = Depends(get_db)):
    return get_all_users(db)