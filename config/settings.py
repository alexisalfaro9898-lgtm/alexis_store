import os
from pathlib import Path

# Directorio Base
BASE_DIR = Path(__file__).resolve().parent.parent

# Seguridad
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-alexis-sublimaciones-2026-v1')
DEBUG = False
ALLOWED_HOSTS = ['araa.store', 'www.araa.store', '127.0.0.1', '.onrender.com']

# Aplicaciones
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'catalogo',
    'django_cleanup.apps.CleanupConfig',
]

# Middlewares
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(BASE_DIR, 'templates')],
    'APP_DIRS': True,
    'OPTIONS': {'context_processors': [
        'django.template.context_processors.debug',
        'django.template.context_processors.request',
        'django.contrib.auth.context_processors.auth',
        'django.contrib.messages.context_processors.messages',
    ]},
}]

# Base de datos SQLite
DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': BASE_DIR / 'db.sqlite3'}}

# Idioma y Hora (Uruguay)
LANGUAGE_CODE = 'es-uy'
TIME_ZONE = 'America/Montevideo'
USE_I18N = True
USE_TZ = True

# Archivos Estáticos (CSS, JS)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# --- CONFIGURACIÓN DE IMÁGENES (MEDIA) ---
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'CATALOGO_LIMPIO_DISER')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --- LLAVE MAESTRA (Crear Admin y Cargar Productos) ---
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def setup_tienda(sender, **kwargs):
    if sender.name == 'catalogo':
        from django.contrib.auth.models import User
        # Crear admin si no existe
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@araa.store', 'Alexis2026!')
        
        # Ejecutar carga automática de catálogo
        script_carga = os.path.join(BASE_DIR, "cargar_catalogo.py")
        if os.path.exists(script_carga):
            import subprocess
            try:
                subprocess.run(["python", "cargar_catalogo.py"], check=True)
                print("Catálogo cargado exitosamente.")
            except Exception as e:
                print(f"Error al ejecutar script: {e}")
