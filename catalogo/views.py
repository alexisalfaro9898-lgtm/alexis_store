from django.shortcuts import render, get_object_split, redirect
from .models import Producto, Categoria, Carrito, ItemCarrito

def index(request):
    # Traemos todas las categorías para mostrarlas en el catálogo
    categorias = Categoria.objects.all()
    # Obtenemos el total de items para el icono del carrito en el navbar
    session_id = request.session.session_key
    total_items = 0
    if session_id:
        carrito = Carrito.objects.filter(session_id=session_id).first()
        if carrito:
            total_items = sum(item.cantidad for item in carrito.itemcarrito_set.all())
    
    return render(request, 'index.html', {
        'categorias': categorias,
        'total_items': total_items
    })

def agregar_al_carrito(request, producto_id):
    if not request.session.session_key:
        request.session.create()
    
    session_id = request.session.session_key
    producto = get_object_or_404(Producto, id=producto_id)
    carrito, _ = Carrito.objects.get_or_create(session_id=session_id)
    
    item, created = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)
    if not created:
        item.cantidad += 1
        item.save()
    
    return redirect('index')

def ver_carrito(request):
    session_id = request.session.session_key
    carrito = None
    items = []
    total = 0
    if session_id:
        carrito = Carrito.objects.filter(session_id=session_id).first()
        if carrito:
            items = carrito.itemcarrito_set.all()
            total = sum(item.producto.precio * item.cantidad for item in items)
            
    return render(request, 'carrito.html', {'items': items, 'total': total})

def eliminar_del_carrito(request, item_id):
    item = get_object_or_404(ItemCarrito, id=item_id)
    item.delete()
    return redirect('ver_carrito')
    
