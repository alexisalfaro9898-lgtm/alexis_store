from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), # Corregido: .urls en lugar de .path
    path('', include('catalogo.urls')),
]

# Esto sirve las imágenes en Render (cuando DEBUG es False)
if not settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

