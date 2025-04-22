import os


def create_module(name: str):
    # Membuat path modul di folder 'app' di root project
    module_path = os.path.join("app", name)

    # Membuat folder untuk modul jika belum ada
    os.makedirs(module_path, exist_ok=True)

    # Daftar file dan template yang akan dibuat
    files = {
        f"{name}_model.py": f"# {name.capitalize()} Model\n",
        f"{name}_service.py": f"# {name.capitalize()} Service\n",
        f"{name}_controller.py": f"# {name.capitalize()} Controller\n",
        f"{name}_router.py": f"""# {name.capitalize()} Router
from fastapi import APIRouter

router = APIRouter(
    prefix="/{name}",
    tags=["{name}"]
)

@router.get("/")
def get_{name}s():
    return ["Contoh data {name}"]
"""
    }

    # Menulis file template untuk masing-masing file modul
    for filename, content in files.items():
        file_path = os.path.join(module_path, filename)
        with open(file_path, "w") as f:
            f.write(content)

    print(f"✅ Module '{name}' berhasil dibuat di {module_path}/")


if __name__ == "__main__":
    # Input nama modul yang ingin digenerate
    module_name = input("Masukkan nama module yang ingin digenerate: ").strip()
    if module_name:
        create_module(module_name.lower())
    else:
        print("❌ Nama module tidak boleh kosong.")
