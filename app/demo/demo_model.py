from sqlalchemy import Column, Integer, String
from config.database import Base


class DemoModel(Base):
    __tablename__ = "demo"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)


from pydantic import BaseModel

class DemoSchema(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True  # Untuk mendukung ORM (SQLAlchemy)

class DemoCreateSchema(BaseModel):
    name: str
