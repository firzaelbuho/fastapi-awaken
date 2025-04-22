from sqlalchemy import Column, Integer, String
from config.database import Base
from pydantic import BaseModel


class PrimoidModel(Base):
    __tablename__ = "primoid"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)


class PrimoidSchema(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class PrimoidCreateSchema(BaseModel):
    name: str
