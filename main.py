from fastapi import FastAPI
from app.demo import  demo_router
from app.character import character_router
from app.primoid import primoid_router
from app.primoid_type import primoid_type_router
from app.primoid_category import primoid_category_router


app = FastAPI()

# Create tables (optional: untuk dev lokal)
# Base.metadata.create_all(bind=engine)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# You can add additional URLs to this list, for example, the frontend's production domain, or other frontends.
allowed_origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["X-Requested-With", "Content-Type"],
)


app.include_router(character_router.router)
app.include_router(demo_router.router)
app.include_router(primoid_router.router)
app.include_router(primoid_type_router.router)
app.include_router(primoid_category_router.router)


