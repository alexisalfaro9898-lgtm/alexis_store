from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('eliminar/<int:item_id>/', views.eliminar_del_carrito, name='eliminar'),
]
