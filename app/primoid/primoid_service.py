from sqlalchemy.orm import Session
from app.primoid.primoid_model import PrimoidModel


def get_all_primoids(db: Session):
    return db.query(PrimoidModel).all()



