from sqlalchemy import Column, Integer, String, Text, ForeignKey
from config.database import Base


class PrimoidModel(Base):
    __tablename__ = "primoid"

    primoid_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, index=True)
    alternate_name = Column(String(100))
    primoid_category_id = Column(Integer, ForeignKey("primoid_category.primoid_category_id"), nullable=False)
    primoid_type_id = Column(Integer, ForeignKey("primoid_type.primoid_type_id"), nullable=False)
    description = Column(Text)
from pydantic import BaseModel
from typing import Optional


class PrimoidSchema(BaseModel):
    primoid_id: int
    name: str
    alternate_name: Optional[str] = None
    primoid_category_id: int
    primoid_type_id: int
    description: Optional[str] = None

    class Config:
        from_attributes = True
