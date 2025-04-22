# Character Router
from fastapi import APIRouter

router = APIRouter(
    prefix="/character",
    tags=["character"]
)

@router.get("/")
def get_characters():
    return ["Contoh data character"]
