import os
import django
from pathlib import Path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from catalogo.models import Producto, Categoria

BASE_DIR = Path(__file__).resolve().parent
RUTA_FOTOS = os.path.join(BASE_DIR, 'CATALOGO_LIMPIO_DISER')

def cargar():
    if not os.path.exists(RUTA_FOTOS):
        print("Error: No se encontró la carpeta CATALOGO_LIMPIO_DISER")
        return

    # IMPORTANTE: Borramos lo viejo para que no haya duplicados sin foto
    Producto.objects.all().delete()
    Categoria.objects.all().delete()

    for nombre_cat in os.listdir(RUTA_FOTOS):
        ruta_cat = os.path.join(RUTA_FOTOS, nombre_cat)
        if os.path.isdir(ruta_cat):
            cat_obj, _ = Categoria.objects.get_or_create(nombre=nombre_cat)
            
            for archivo in os.listdir(ruta_cat):
                if archivo.lower().endswith(('.png', '.jpg', '.jpeg')):
                    nombre_prod = archivo.split('.')[0]
                    # Aquí está el truco: le decimos a Django dónde está la foto
                    Producto.objects.create(
                        nombre=nombre_prod,
                        categoria=cat_obj,
                        precio=0,
                        imagen=f'CATALOGO_LIMPIO_DISER/{nombre_cat}/{archivo}'
                    )
    print("Sincronización completa.")

if __name__ == '__main__':
    cargar()
