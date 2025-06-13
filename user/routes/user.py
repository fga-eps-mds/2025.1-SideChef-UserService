from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from user.schemas.user import UserCreate, UserOut

from user.services.user import create_user

from core.database import get_db

from user.services.user import create_user, get_all_users, delete_user
from typing import List


from fastapi import HTTPException

import traceback

router = APIRouter()

@router.post("/", response_model=UserOut, status_code=201)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.get("/", response_model=List[UserOut])
def list_users(db: Session = Depends(get_db)):
    return get_all_users(db)


@router.delete("/{user_id}", status_code=204)
def delete_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    try:
        success = delete_user(db, user_id)
        if not success:
            raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
