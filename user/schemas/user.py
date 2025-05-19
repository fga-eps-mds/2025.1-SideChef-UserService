from pydantic import BaseModel, EmailStr, constr, conint, AwareDatetime
from datetime import datetime


class UserCreate(BaseModel):
    name: str                      # Nome simples
    password: str                  # Senha como string simples
    email: EmailStr                # Valida e-mail automaticamente
    cpf: str                       # Inteiro positivo (para evitar CPF = 0)

class UserOut(BaseModel):
    id: int
    name: str
    password: str
    email: EmailStr
    cpf: str
    created_at: AwareDatetime

    class Config:
        orm_mode = True
