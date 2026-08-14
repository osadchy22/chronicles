from enum import Enum

class ItemType(str, Enum):
    RESOURCE = "resource"
    EQUIPMENT = "equipment"
    CONSUMABLE ="comsumable"
    QUEST = "quest"
    MATERIAL = "material"

class Rarity(srt, Enum):
    COMMON = "common"
    UNCOMMON = "uncommon"
    RARE = "rare"
    EPIC = "epic"
    LEGENDARY = "legendary"
    MYTHIC = "mythic"