import os
from pathlib import Path

# 1. Definir la base
BASE_DIR = Path(__file__).resolve().parent.parent

# 2. Definir DEBUG y SECRET_KEY (IMPORTANTE: antes de usarlas abajo)
DEBUG = False  # Cambialo a True si querés ver errores detallados en la web
SECRET_KEY = 'django-insecure-tu-clave-aqui' 

# 3. Ahora sí, los hosts
ALLOWED_HOSTS = [
    'araa.store', 
    'www.araa.store', 
    '127.0.0.1', 
    '.onrender.com'
]

# ... resto del código (INSTALLED_APPS, etc.) ...
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',  # <--- REVISÁ QUE ESTA LÍNEA ESTÉ AQUÍ
    # ... tus otras apps (catalogo, etc.) ...
]
# 4. Al final del archivo, donde tenías el error:
if not DEBUG:
    SECRET_KEY = os.environ.get('SECRET_KEY', SECRET_KEY)
