from fastapi import FastAPI
from app.demo import  demo_router
from app.character import character_router

app = FastAPI()

# Create tables (optional: untuk dev lokal)
# Base.metadata.create_all(bind=engine)
app.include_router(character_router.router)
app.include_router(demo_router.router)

