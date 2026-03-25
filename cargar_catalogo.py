import os, django, random
from django.core.files import File

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from catalogo.models import Categoria, Producto

def importar():
    ruta_base = '/home/kali/CATALOGO_LIMPIO_DISER'
    if not os.path.exists(ruta_base):
        print(f"Error: No se encontró la carpeta en {ruta_base}")
        return

    # Escanea las carpetas dentro de CATALOGO_LIMPIO_DISER
    for carpeta in os.listdir(ruta_base):
        ruta_carpeta = os.path.join(ruta_base, carpeta)
        
        if os.path.isdir(ruta_carpeta):
            # Crea la categoría (ej: "Tazas", "Remeras")
            cat, _ = Categoria.objects.get_or_create(nombre=carpeta)
            print(f"Procesando categoría: {carpeta}...")
            
            for archivo in os.listdir(ruta_carpeta):
                if archivo.lower().endswith(('.png', '.jpg', '.jpeg')):
                    # Limpiamos el nombre para que quede lindo en la web
                    nombre_prod = archivo.split('.')[0].replace('_', ' ').replace('-', ' ')
                    
                    if not Producto.objects.filter(nombre=nombre_prod, categoria=cat).exists():
                        p = Producto(
                            categoria=cat, 
                            nombre=nombre_prod, 
                            precio=random.randint(150, 600)
                        )
                        with open(os.path.join(ruta_carpeta, archivo), 'rb') as f:
                            p.imagen.save(archivo, File(f), save=True)
            print(f"✅ Carpeta '{carpeta}' completada.")
            
    print("\n--- ¡Todo el catálogo de DISER ha sido importado con éxito! ---")

if __name__ == '__main__':
    importar()
