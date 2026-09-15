import json
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.auth.telegram import validate_telegram_init_data
from app.config import settings
from app.database.session import get_db
from app.models.character import Character
from app.models.user import User
from app.schemas.auth import AuthResponse, TelegramAuthRequest

router = APIRouter(
    prefix="/api/auth",
    tags=["auth"],
)

@router.get("/test")
def test_auth():
    return {"status": "auth works"}

@router.post(
    "/telegram",
    response_model=AuthResponse,
)
def authenticate_telegram(
    request: TelegramAuthRequest,
    db: Session = Depends(get_db),
):
    telegram_data = validate_telegram_init_data(
        request.init_data,
        settings.telegram_bot_token,
    )

    user_data_raw = telegram_data.get("user")

    if not user_data_raw:
        raise HTTPException(
            status_code=401,
            detail="Telegram user data is missing",
        )

    try:
        telegram_user = json.loads(user_data_raw)
    except json.JSONDecodeError:
        raise HTTPException(
            status_code=401,
            detail="Invalid Telegram user data",
        )

    telegram_id = telegram_user.get("id")

    if telegram_id is None:
        raise HTTPException(
            status_code=401,
            detail="Telegram user id is missing",
        )

    try:
        telegram_id = int(telegram_id)
    except (TypeError, ValueError):
        raise HTTPException(
            status_code=401,
            detail="Invalid Telegram user id",
        )

    username = telegram_user.get("username")
    first_name = telegram_user.get("first_name")

    user = db.scalar(
        select(User).where(
            User.telegram_id == telegram_id
        )
    )

    now = datetime.now(timezone.utc)

    if user is None:
        user = User(
            telegram_id=telegram_id,
            username=username,
            first_name=first_name,
            created_at=now,
            last_login_at=now,
            is_banned=False,
            is_admin=False,
        )

        db.add(user)
        db.flush()

    else:
        if user.is_banned:
            raise HTTPException(
                status_code=403,
                detail="User is banned",
            )

        user.username = username
        user.first_name = first_name
        user.last_login_at = now

        db.flush()

    character = db.scalar(
        select(Character).where(
            Character.user_id == user.id
        )
    )

    if character is None:
        character_name = first_name or username or "Adventurer"

        character = Character(
            user_id=user.id,
            name=character_name,
            level=1,
            experience=0,
            gold=100,
            reserved_gold=0,
            energy=100,
            max_energy=100,
            hp=100,
            max_hp=100,
            strength=5,
            vitality=5,
            agility=5,
            intelligence=5,
            luck=5,
            created_at=now,
            updated_at=now,
        )

        db.add(character)
        db.flush()

    db.commit()

    return AuthResponse(
        user_id=user.id,
        character_id=character.id,
        character_name=character.name,
    )