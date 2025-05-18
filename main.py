from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from core.config_loader import settings
from user.routes.user import router as user_router  # Corrigido

app = FastAPI()

# Middleware CORS
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin).strip("/") for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# Rotas
app.include_router(user_router, prefix='/api/users', tags=['Users'])

# Health check
@app.get("/health", tags=['Health Checks'])
def read_root():
    return {"APP": "Running"}
