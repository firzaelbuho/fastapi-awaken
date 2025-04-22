from fastapi import HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.primoid.primoid_model import PrimoidSchema
from app.primoid import primoid_service


def handle_get_all_primoids(db: Session) -> List[PrimoidSchema]:
    try:
        return primoid_service.get_all_primoids(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
