import hashlib
import hmac
import json
import time
from urllib.parse import parse_qsl

from app.config import settings

def validate_telegram_init_data(
    init_data: str,
    max_age: int = 86400,
) -> dict:
    parsed = dict(parse_qsl(init_data, keep_blank_values=True))

    received_hash = parsed.pop("hash", None)

    if not received_hash:
        raise ValueError("Missing Telegram hash")

    auth_date = int(parsed.get("auth_date", 0))

    if auth_date <= 0:
        raise ValueError("Invalid auth_date")

    if time.time() - auth_date > max_age:
        raise ValueError("Telegram init data expired")

    data_check_string = "\n".join(
        f"{key}={value}"
        for key, value in sorted(parsed.items())
    )

    secret_key = hmac.new(
        b"WebAppData",
        settings.telegram_bot_token.encode(),
        hashlib.sha256,
    ).digest()

    calculated_hash = hmac.new(
        secret_key,
        data_check_string.encode(),
        hashlib.sha256,
    ).hexdigest()

    if not hmac.compare_digest(
        calculated_hash,
        received_hash,
    ):
        raise ValueError("Invalid Telegram signature")

    user_raw = parsed.get("user")

    if not user_raw:
        raise ValueError("Telegram user missing")

    user = json.loads(user_raw)

    return {
        "telegram_id": int(user["id"]),
        "username": user.get("username"),
        "first_name": user.get("first_name"),
    }