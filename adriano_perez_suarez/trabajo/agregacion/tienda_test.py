import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from tienda import Tienda
from producto import Producto

# --------------------
# Test de instancia
# --------------------
def test_instancia_tienda():
    tienda = Tienda("Tienda Central")
    producto = Producto("Laptop", 1200)

    assert isinstance(tienda, Tienda)
    assert isinstance(producto, Producto)

def test_lista_productos_vacia():
    tienda = Tienda("Tienda Vacía")

    assert tienda.productos == []
    # o también:
    assert len(tienda.productos) == 0
# --------------------
# Test de atributos
# --------------------
def test_atributos_producto():
    producto = Producto("Mouse", 25)
    assert producto.nombre == "Mouse"
    assert producto.precio == 25

# --------------------
# Test de métodos
# --------------------
def test_agregar_y_mostrar_productos():
    tienda = Tienda("Tienda Central")
    producto1 = Producto("Laptop", 1200)
    producto2 = Producto("Teclado", 50)

    tienda.agregar_producto(producto1)
    tienda.agregar_producto(producto2)

    lista_productos = tienda.mostrar_productos()

    assert "Laptop - $1200" in lista_productos
    assert "Teclado - $50" in lista_productos
def test_lista_productos_llena():
    tienda = Tienda("Tienda Central")
    producto = Producto("Laptop", 1200)

    tienda.agregar_producto(producto)

    assert tienda.productos           
    assert len(tienda.productos) > 0