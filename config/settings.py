# 1. Permitir que Render vea la web
ALLOWED_HOSTS = [
    'araa.store', 
    'www.araa.store', 
    '127.0.0.1', 
    '.onrender.com'  # <-- Agregá esto para que funcione en Render
]

# 2. Configuración de archivos estáticos para el servidor
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # <-- Agregá esto
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# 3. Seguridad para producción (opcional pero recomendado)
if not DEBUG:
    SECRET_KEY = os.environ.get('SECRET_KEY', SECRET_KEY)
