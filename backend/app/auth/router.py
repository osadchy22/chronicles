from fastapi import APIRouter

from app.core.config import settings
from app.auth.telegram import validate_telegram_init_data

router = APIRouter(
    prefix="/api/auth",
    tags=["auth"],
)

@router.get("/test")
def auth_test():
    return {
        "status": "ok",
        "service": "auth",
    }

@router.post("/telegram")
def telegram_auth(init_data: str):
    if not settings.TELEGRAM_BOT_TOKEN:
        raise RuntimeError("TELEGRAM_BOT_TOKEN is not configured")

    telegram_data = validate_telegram_init_data(
        init_data,
        settings.TELEGRAM_BOT_TOKEN,
    )

    return {
        "status": "ok",
        "telegram_data": telegram_data,
    }