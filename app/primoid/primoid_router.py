from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.primoid.primoid_model import PrimoidSchema
from app.primoid import primoid_controller
from config.database import get_db


router = APIRouter(prefix="/primoid", tags=["primoid"])


@router.get("/", response_model=List[PrimoidSchema])
def read_primoids(db: Session = Depends(get_db)):
    return primoid_controller.handle_get_all_primoids(db)
