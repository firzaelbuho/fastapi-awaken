from sqlalchemy import Column, Integer, String, Text
from config.database import Base
from pydantic import BaseModel
from typing import Optional


class PrimoidCategoryModel(Base):
    __tablename__ = "primoid_category"

    primoid_category_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    rank = Column(String(1))
    alternate_name = Column(String(100))
    description = Column(Text)
    handling = Column(Text)


class PrimoidCategorySchema(BaseModel):
    primoid_category_id: int
    name: str
    rank: Optional[str] = None
    alternate_name: Optional[str] = None
    description: Optional[str] = None
    handling: Optional[str] = None

    class Config:
        from_attributes = True


class PrimoidCategoryCreateSchema(BaseModel):
    name: str
    rank: Optional[str] = None
    alternate_name: Optional[str] = None
    description: Optional[str] = None
    handling: Optional[str] = None
