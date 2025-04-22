from sqlalchemy.orm import Session
from app.demo.demo_model import DemoModel, DemoCreateSchema, DemoSchema


def get_all_demos(db: Session):
    return db.query(DemoModel).all()

def create_demo(db: Session, demo_data: DemoCreateSchema):
    new_demo = DemoSchema(name=demo_data.name)
    db.add(new_demo)
    db.commit()
    db.refresh(new_demo)
    return new_demo
