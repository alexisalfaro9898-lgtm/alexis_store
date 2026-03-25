MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # <-- AGREGÁ ESTA LÍNEA
    'django.contrib.sessions.middleware.SessionMiddleware',
    # ... los demás siguen igual
]
