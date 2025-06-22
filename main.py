from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from core.config_loader import settings
from user.routes.user import router as user_router  # Caminho corrigido
from user.models.user import Base
from core.database import engine
from fastapi.middleware.cors import CORSMiddleware


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],
)


app.include_router(user_router, prefix="/api/users", tags=["Users"])

@app.get("/health", tags=["Health Checks"])
def read_root():
    return {"APP": "Running"}
