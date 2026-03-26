# cargar_inicial.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from catalogo.models import Producto

productos = [
    {"nombre": "Taza Blanca (Stock)", "precio": 150, "desc": "Entrega inmediata."},
    {"nombre": "Taza Blanca Personalizada", "precio": 180, "desc": "Diseño a elección."},
    {"nombre": "Taza Especial (Glitter/Mágica/Color)", "precio": 250, "desc": "Incluye variantes con cuchara o interior de color."},
    {"nombre": "Body de Bebé (Talles 00 al 12)", "precio": 360, "desc": "Disponibles en talle 00, 03, 06, 09 y 12."},
    {"nombre": "Remera Blanca (Stock)", "precio": 250, "desc": "Talles disponibles en stock."},
    {"nombre": "Remera Blanca (Por encargo)", "precio": 450, "desc": "Pedido personalizado."},
    {"nombre": "Remera Color/Algodón (Stock)", "precio": 450, "desc": "Varios colores disponibles."},
]

for p in productos:
    Producto.objects.get_or_create(
        nombre=p['nombre'],
        defaults={'precio': p['precio'], 'descripcion': p['desc'], 'stock': 10}
    )

print("¡Productos de Alexis Sublimaciones cargados con éxito!")
