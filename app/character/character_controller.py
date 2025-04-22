from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.character.character_model import  CharacterSchema
from app.character import character_service
from typing import List



def handle_get_all_characters(db: Session) -> List[CharacterSchema]:
    try:
        return character_service.get_all_characters(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

