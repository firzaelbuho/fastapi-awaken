from fastapi import FastAPI
from app.demo import demo_router
from config.database import Base, engine

app = FastAPI()

# Create tables (optional: untuk dev lokal)
# Base.metadata.create_all(bind=engine)

app.include_router(demo_router.router)
