class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Carrito:
    def __init__(self):
        self.productos = []
        
    def add(self, producto):
        if isinstance(producto, Producto):
            self.productos.append(producto)
        

class Motor:
    def __init__(self, potencia):
        self.potencia = potencia
        
class Carro:
    def __init__(self, motor_potencia):
        self.motor = Motor(motor_potencia)
        

                