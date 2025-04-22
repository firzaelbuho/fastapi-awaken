# Character Model
from sqlalchemy import Column, Integer, String, Date, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class CharacterModel(Base):
    __tablename__ = 'character'

    character_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    birthdate = Column(Date, nullable=False)
    gender = Column(String(10), nullable=False)
    description = Column(Text, nullable=True)

# Pydantic Schema untuk Character
from pydantic import BaseModel
from datetime import date  # Pas

class CharacterSchema(BaseModel):
    character_id: int
    name: str
    birthdate: date
    gender: str
    description: str | None = None  # Optional field, bisa None

    class Config:
        from_attributes = True  # Untuk mendukung ORM (SQLAlchemy)
