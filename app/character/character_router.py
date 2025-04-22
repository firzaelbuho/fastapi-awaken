from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.character.character_model import CharacterSchema
from app.character import character_controller
from config.database import  get_db


router = APIRouter(prefix="/character", tags=["character"])

@router.get("/", response_model=List[CharacterSchema])
def read_characters(db: Session = Depends(get_db)):
    return character_controller.handle_get_all_characters(db)

# @router.post("/", response_model=DemoSchema)
# def add_demo(demo: DemoCreate, db: Session = Depends(get_db)):
#     return demo_controller.handle_create_demo(demo, db)
