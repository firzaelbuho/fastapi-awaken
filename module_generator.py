# import os
#
#
# def create_module(name: str):
#     # Membuat path modul di folder 'app' di root project
#     module_path = os.path.join("app", name)
#
#     # Membuat folder untuk modul jika belum ada
#     os.makedirs(module_path, exist_ok=True)
#
#     # Daftar file dan template yang akan dibuat
#     files = {
#         f"{name}_model.py": f"# {name.capitalize()} Model\n",
#         f"{name}_service.py": f"# {name.capitalize()} Service\n",
#         f"{name}_controller.py": f"# {name.capitalize()} Controller\n",
#         f"{name}_router.py": f"""# {name.capitalize()} Router
# from fastapi import APIRouter
#
# router = APIRouter(
#     prefix="/{name}",
#     tags=["{name}"]
# )
#
# @router.get("/")
# def get_{name}s():
#     return ["Contoh data {name}"]
# """
#     }
#
#     # Menulis file template untuk masing-masing file modul
#     for filename, content in files.items():
#         file_path = os.path.join(module_path, filename)
#         with open(file_path, "w") as f:
#             f.write(content)
#
#     print(f"✅ Module '{name}' berhasil dibuat di {module_path}/")
#
#
# if __name__ == "__main__":
#     # Input nama modul yang ingin digenerate
#     module_name = input("Masukkan nama module yang ingin digenerate: ").strip()
#     if module_name:
#         create_module(module_name.lower())
#     else:
#         print("❌ Nama module tidak boleh kosong.")



import os


def create_module(name: str):
    class_name = name.capitalize()
    schema_name = f"{class_name}Schema"
    create_schema_name = f"{class_name}CreateSchema"
    model_name = f"{class_name}Model"

    module_path = os.path.join("app", name)
    os.makedirs(module_path, exist_ok=True)

    files = {
        f"{name}_model.py": f"""from sqlalchemy import Column, Integer, String
from config.database import Base
from pydantic import BaseModel


class {model_name}(Base):
    __tablename__ = "{name}"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)


class {schema_name}(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class {create_schema_name}(BaseModel):
    name: str
""",

        f"{name}_service.py": f"""from sqlalchemy.orm import Session
from app.{name}.{name}_model import {model_name}, {create_schema_name}, {schema_name}


def get_all_{name}s(db: Session):
    return db.query({model_name}).all()


def create_{name}(db: Session, data: {create_schema_name}):
    new_item = {model_name}(name=data.name)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item
""",

        f"{name}_controller.py": f"""from fastapi import HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.{name}.{name}_model import {schema_name}
from app.{name} import {name}_service


def handle_get_all_{name}s(db: Session) -> List[{schema_name}]:
    try:
        return {name}_service.get_all_{name}s(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
""",

        f"{name}_router.py": f"""from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.{name}.{name}_model import {schema_name}
from app.{name} import {name}_controller
from config.database import get_db


router = APIRouter(prefix="/{name}", tags=["{name}"])


@router.get("/", response_model=List[{schema_name}])
def read_{name}s(db: Session = Depends(get_db)):
    return {name}_controller.handle_get_all_{name}s(db)
"""
    }

    for filename, content in files.items():
        file_path = os.path.join(module_path, filename)
        with open(file_path, "w") as f:
            f.write(content)

    print(f"✅ Module '{name}' berhasil dibuat di {module_path}/")


if __name__ == "__main__":
    module_name = input("Masukkan nama module yang ingin digenerate: ").strip()
    if module_name:
        create_module(module_name.lower())
    else:
        print("❌ Nama module tidak boleh kosong.")

