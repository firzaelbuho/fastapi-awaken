from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import SessionLocal
from app.demo import demo_service
from app.demo.demo_model import DemoSchema, DemoCreate
from typing import List

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def handle_get_all_demos(db: Session) -> List[DemoSchema]:
    try:
        return demo_service.get_all_demos(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def handle_create_demo(demo: DemoCreate, db: Session) -> DemoSchema:
    try:
        return demo_service.create_demo(db, demo)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
