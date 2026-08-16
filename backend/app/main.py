from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import auth, character
from app.config import settings

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origin_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(character.router)

@app.get("/api/health")
def health():
    return {
        "status": "ok",
        "service": "chronicles-backend",
    }
