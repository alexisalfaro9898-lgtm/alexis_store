# Configuración de archivos estáticos y multimedia
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = '/media/'
# Esta es la ruta única y correcta para tus fotos
MEDIA_ROOT = os.path.join(BASE_DIR, 'CATALOGO_LIMPIO_DISER')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --- AUTO-CONFIGURACIÓN (LLAVE MAESTRA) ---
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def setup_tienda(sender, **kwargs):
    if sender.name == 'catalogo':
        from django.contrib.auth.models import User
        # Crear superusuario si no existe
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@araa.store', 'Alexis2026!')
        
        # Ejecutar script de carga de productos
        script_carga = os.path.join(BASE_DIR, "cargar_catalogo.py")
        if os.path.exists(script_carga):
            import subprocess
            try:
                subprocess.run(["python", "cargar_catalogo.py"], check=True)
            except Exception as e:
                print(f"Error al cargar catálogo: {e}")
