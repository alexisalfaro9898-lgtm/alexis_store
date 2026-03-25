from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    def __str__(self):
        return self.nombre

# --- ESTO ES LO QUE FALTA ---
class Carrito(models.Model):
    session_id = models.CharField(max_length=255, unique=True)
    creado_en = models.DateTimeField(auto_now_add=True)

class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
