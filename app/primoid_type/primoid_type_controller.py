from fastapi import HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.primoid_type.primoid_type_model import PrimoidTypeSchema, PrimoidTypeCreateSchema
from app.primoid_type import primoid_type_service


def handle_get_all_primoid_types(db: Session) -> List[PrimoidTypeSchema]:
    try:
        return primoid_type_service.get_all_primoid_types(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def handle_create_primoid_type(db: Session, data: PrimoidTypeCreateSchema) -> PrimoidTypeSchema:
    try:
        return primoid_type_service.create_primoid_type(db, data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
