from pydantic import BaseModel

class CharacterResponse(BaseModel):
    id: int
    name: str

    level: int
    experience: int

    gold: int
    reserved_gold: int

    energy: int
    max_energy: int

    hp: int
    max_hp: int

    strength: int
    vitality: int
    agility: int
    intelligence: int
    luck: int

    model_config = {
        "from_attributes": True
    }