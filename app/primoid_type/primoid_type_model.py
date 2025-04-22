from sqlalchemy import Column, Integer, String, Text
from config.database import Base
from pydantic import BaseModel
from typing import Optional


class PrimoidTypeModel(Base):
    __tablename__ = "primoid_type"
    primoid_type_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    alternate_name = Column(String(100))
    description = Column(Text)
    handling = Column(Text)


class PrimoidTypeSchema(BaseModel):
    primoid_type_id: int
    name: str
    alternate_name: Optional[str] = None
    description: Optional[str] = None
    handling: Optional[str] = None

    class Config:
        from_attributes = True


class PrimoidTypeCreateSchema(BaseModel):
    name: str
    alternate_name: Optional[str] = None
    description: Optional[str] = None
    handling: Optional[str] = None
