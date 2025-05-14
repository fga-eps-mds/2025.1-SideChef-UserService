from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from core.config_loader import settings
from pydantic import BaseModel, EmailStr

from user.routes.user import user_router


app = FastAPI()

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            str(origin).strip("/") for origin in settings.BACKEND_CORS_ORIGINS
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(user_router, prefix='/api', tags=['Users'])

@app.get("/health", tags=['Health Checks'])
def read_root():
    return {"APP": "Running"}

# Schema do usuário
class User(BaseModel):
    name: str
    email: EmailStr


# Lista para armazenar os usuários criados temporariamente (apenas para teste)
users_db = []

# Endpoint POST para criar usuário
@app.post("/users")
def create_user(user: User):
    users_db.append(user)  # Adiciona o usuário na "base de dados" temporária
    return {
        "message": "Usuário criado com sucesso!",
        "user": user
    }


# Endpoint GET para listar todos os usuários
@app.get("/users")
def get_users():
    return users_db  # Retorna todos os usuários criados

# Deletar usuário por email
@app.delete("/users/{email}")
def delete_user(email: EmailStr):
    for i, user in enumerate(users_db):
        if user.email == email:
            del users_db[i]
            return {"message": f"Usuário com email {email} foi deletado com sucesso."}
    raise HTTPException(status_code=404, detail="Usuário não encontrado.")