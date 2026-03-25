import os
from pathlib import Path

# ESTA ES LA LÍNEA QUE FALTA:
BASE_DIR = Path(__file__).resolve().parent.parent

# ... Ahora sí, lo que ya tenías:
ALLOWED_HOSTS = [
    'araa.store', 
    'www.araa.store', 
    '127.0.0.1', 
    '.onrender.com'
]

# 2. Configuración de archivos estáticos
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
# 3. Seguridad para producción (opcional pero recomendado)
if not DEBUG:
    SECRET_KEY = os.environ.get('SECRET_KEY', SECRET_KEY)
