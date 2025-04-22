from sqlalchemy.orm import Session
from app.primoid.primoid_model import PrimoidModel, PrimoidCreateSchema, PrimoidSchema


def get_all_primoids(db: Session):
    return db.query(PrimoidModel).all()


def create_primoid(db: Session, data: PrimoidCreateSchema):
    new_item = PrimoidModel(name=data.name)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item
