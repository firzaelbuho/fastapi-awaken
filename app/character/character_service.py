from sqlalchemy.orm import Session
from app.character.character_model import CharacterModel

def get_all_characters(db: Session):
    return db.query(CharacterModel).all()


