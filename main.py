from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from core.config_loader import settings
from user.routes.user import router as user_router  # Caminho corrigido


app = FastAPI()

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin).strip("/") for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(user_router, prefix="/api/users", tags=["Users"])

@app.get("/health", tags=["Health Checks"])
def read_root():
    return {"APP": "Running"}
