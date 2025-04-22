from sqlalchemy.orm import Session
from app.primoid_category.primoid_category_model import PrimoidCategoryModel


def get_all_primoid_categorys(db: Session):
    return db.query(PrimoidCategoryModel).all()



