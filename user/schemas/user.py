from pydantic import BaseModel, EmailStr, constr, conint, AwareDatetime
from datetime import datetime


class UserCreate(BaseModel):
    name: str                      # Name as a simple string
    password: str                  # Password as a simple string
    email: EmailStr                # Automatically validate email
    

class UserOut(BaseModel):
    id: int
    name: str
    password: str
    email: EmailStr
    created_at: AwareDatetime

    class Config:
        orm_mode = True
