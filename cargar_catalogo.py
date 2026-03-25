import os
import django
from pathlib import Path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from catalogo.models import Producto, Categoria

BASE_DIR = Path(__file__).resolve().parent
# Nombre exacto de tu carpeta de fotos
CARPETA_NOMBRE = 'CATALOGO_LIMPIO_DISER'
RUTA_FOTOS = os.path.join(BASE_DIR, CARPETA_NOMBRE)

def cargar():
    if not os.path.exists(RUTA_FOTOS):
        print(f"ERROR: No se encuentra la carpeta {CARPETA_NOMBRE} en el proyecto.")
        return

    for nombre_cat in os.listdir(RUTA_FOTOS):
        ruta_cat = os.path.join(RUTA_FOTOS, nombre_cat)
        if os.path.isdir(ruta_cat):
            cat_obj, _ = Categoria.objects.get_or_create(nombre=nombre_cat)
            for archivo in os.listdir(ruta_cat):
                if archivo.lower().endswith(('.png', '.jpg', '.jpeg')):
                    # Crea el producto si no existe
                    nombre_prod = archivo.split('.')[0].replace('_', ' ')
                    Producto.objects.get_or_create(
                        nombre=nombre_prod,
                        categoria=cat_obj,
                        precio=0 # Ajustalo después en el admin
                    )
    print("¡Carga completada con éxito!")

if __name__ == '__main__':
    cargar()
