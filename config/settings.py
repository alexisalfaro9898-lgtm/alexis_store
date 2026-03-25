import os
from pathlib import Path

# 1. Definir la base
BASE_DIR = Path(__file__).resolve().parent.parent

# 2. Seguridad y Debug
DEBUG = False 
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-alexis-sublimaciones-2026-v1')

# 3. Hosts permitidos
ALLOWED_HOSTS = [
    'araa.store', 
    'www.araa.store', 
    '127.0.0.1', 
    '.onrender.com'
]

# 4. Aplicaciones
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',  # Manejo de archivos estáticos
    'catalogo',                    # Tu aplicación de productos
    'django_cleanup.apps.CleanupConfig',
]

# 5. Middleware (Importante el orden de WhiteNoise)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Sirve archivos estáticos en Render
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 6. Configuración de archivos estáticos (Lo que faltaba)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Configuración de almacenamiento para WhiteNoise
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# 7. URL principal
ROOT_URLCONF = 'config.urls'

# 8. Base de datos (SQLite para empezar)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# 9. Plantillas (Templates)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# 10. Validación de contraseñas
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# 11. Idioma y Zona Horaria (Configurado para Uruguay)
LANGUAGE_CODE = 'es-uy'
TIME_ZONE = 'America/Montevideo'
USE_I18N = True
USE_TZ = True
# 12. Archivos Multimedia
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 13. Tipo de campo por defecto para IDs
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
