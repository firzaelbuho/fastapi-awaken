from sqlalchemy import Column, Integer, String
from config.database import Base


class Demo(Base):
    __tablename__ = "demo"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)


from pydantic import BaseModel

class DemoSchema(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class DemoCreate(BaseModel):
    name: str
