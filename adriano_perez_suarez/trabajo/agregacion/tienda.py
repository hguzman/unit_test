from producto import Producto
#si
class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []  # lista vacía de productos

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        return [str(producto) for producto in self.productos]
