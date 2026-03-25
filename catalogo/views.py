from django.shortcuts import render, get_object_or_404, redirect
import urllib.parse

def home(request):
    from .models import Categoria
    categorias = Categoria.objects.all()
    carrito = request.session.get('carrito', {})
    total_items = sum(item['cantidad'] for item in carrito.values())
    return render(request, 'index.html', {
        'categorias': categorias,
        'total_items': total_items
    })

def agregar_al_carrito(request, producto_id):
    from .models import Producto
    producto = get_object_or_404(Producto, id=producto_id)
    carrito = request.session.get('carrito', {})
    p_id = str(producto_id)
    if p_id in carrito:
        carrito[p_id]['cantidad'] += 1
    else:
        carrito[p_id] = {
            'nombre': producto.nombre,
            'precio': float(producto.precio),
            'cantidad': 1,
            'imagen': producto.imagen.url if producto.imagen else ""
        }
    request.session['carrito'] = carrito
    return redirect('home')

def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    total = 0
    mensaje = "Hola Alexis Sublimaciones, me interesa realizar el siguiente pedido:\n\n"
    
    for id, item in carrito.items():
        subtotal = item['precio'] * item['cantidad']
        total += subtotal
        mensaje += f"- {item['nombre']} (Cant: {item['cantidad']}) - ${subtotal}\n"
    
    mensaje += f"\n*Total: ${total}*"
    mensaje_url = urllib.parse.quote(mensaje)
    
    # CAMBIÁ EL NÚMERO ACÁ ABAJO (Ejemplo: 59899123456)
    whatsapp_url = f"https://wa.me/59896229819?text={mensaje_url}"
    
    return render(request, 'carrito.html', {
        'carrito': carrito, 
        'total': total, 
        'whatsapp_url': whatsapp_url
    })

def limpiar_carrito(request):
    request.session['carrito'] = {}
    return redirect('home')
