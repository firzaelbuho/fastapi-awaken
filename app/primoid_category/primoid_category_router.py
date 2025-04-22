from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.primoid_category.primoid_category_model import PrimoidCategorySchema, PrimoidCategoryCreateSchema
from app.primoid_category import primoid_category_controller
from config.database import get_db


router = APIRouter(prefix="/primoid_category", tags=["primoid_category"])


@router.get("/", response_model=List[PrimoidCategorySchema])
def read_primoid_categorys(db: Session = Depends(get_db)):
    return primoid_category_controller.handle_get_all_primoid_categorys(db)


@router.post("/", response_model=PrimoidCategorySchema)
def create_primoid_category(data: PrimoidCategoryCreateSchema, db: Session = Depends(get_db)):
    return primoid_category_controller.handle_create_primoid_category(db, data)
