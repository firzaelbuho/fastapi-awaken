from fastapi import HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.primoid_category.primoid_category_model import PrimoidCategorySchema, PrimoidCategoryCreateSchema
from app.primoid_category import primoid_category_service


def handle_get_all_primoid_categorys(db: Session) -> List[PrimoidCategorySchema]:
    try:
        return primoid_category_service.get_all_primoid_categorys(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def handle_create_primoid_category(db: Session, data: PrimoidCategoryCreateSchema) -> PrimoidCategorySchema:
    try:
        return primoid_category_service.create_primoid_category(db, data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
