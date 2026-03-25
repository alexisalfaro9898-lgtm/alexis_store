from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from catalogo.views import home, agregar_al_carrito, ver_carrito, limpiar_carrito

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('agregar/<int:producto_id>/', agregar_al_carrito, name='agregar'),
    path('carrito/', ver_carrito, name='ver_carrito'),
    path('limpiar/', limpiar_carrito, name='limpiar_carrito'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
