from sqlalchemy.orm import Session
from app.primoid_type.primoid_type_model import PrimoidTypeModel, PrimoidTypeCreateSchema


def get_all_primoid_types(db: Session):
    return db.query(PrimoidTypeModel).all()



