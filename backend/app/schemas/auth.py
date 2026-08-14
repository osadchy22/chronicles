from pydantic import BaseModel

class TelegramAuthRequest(BaseModel):
    init_data: str

class AuthResponse(BaseModel):
    user_id: int
    character_id: int
    character_name: str