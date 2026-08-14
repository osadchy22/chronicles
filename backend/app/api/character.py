from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.character import Character
from app.schemas.character import CharacterResponse

router = APIRouter(
    prefix="/api/character",
    tags=["character"],
)

@router.get(
    "/{character_id}",
    response_model=CharacterResponse,
)
def get_character(
    character_id: int,
    db: Session = Depends(get_db),
):
    character = db.scalar(
        select(Character).where(
            Character.id == character_id
        )
    )

    if character is None:
        raise HTTPException(
            status_code=404,
            detail="Character not found",
        )

    return character