from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.demo import demo_controller
from app.demo.demo_model import DemoSchema, DemoCreate
from app.demo.demo_controller import get_db

router = APIRouter(prefix="/demo", tags=["demo"])

@router.get("/", response_model=List[DemoSchema])
def read_demos(db: Session = Depends(get_db)):
    return demo_controller.handle_get_all_demos(db)

@router.post("/", response_model=DemoSchema)
def add_demo(demo: DemoCreate, db: Session = Depends(get_db)):
    return demo_controller.handle_create_demo(demo, db)
