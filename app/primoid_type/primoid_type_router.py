from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.primoid_type.primoid_type_model import PrimoidTypeSchema, PrimoidTypeCreateSchema
from app.primoid_type import primoid_type_controller
from config.database import get_db


router = APIRouter(prefix="/primoid_type", tags=["primoid_type"])


@router.get("/", response_model=List[PrimoidTypeSchema])
def read_primoid_types(db: Session = Depends(get_db)):
    return primoid_type_controller.handle_get_all_primoid_types(db)


@router.post("/", response_model=PrimoidTypeSchema)
def create_primoid_type(data: PrimoidTypeCreateSchema, db: Session = Depends(get_db)):
    return primoid_type_controller.handle_create_primoid_type(db, data)
