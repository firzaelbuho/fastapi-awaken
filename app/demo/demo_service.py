from sqlalchemy.orm import Session
from app.demo.demo_model import Demo, DemoCreate

def get_all_demos(db: Session):
    return db.query(Demo).all()

def create_demo(db: Session, demo_data: DemoCreate):
    new_demo = Demo(name=demo_data.name)
    db.add(new_demo)
    db.commit()
    db.refresh(new_demo)
    return new_demo
