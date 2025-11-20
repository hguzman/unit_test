class Producto:
    def __init__(self, nombre, precio):
        if not isinstance(nombre, str):
            raise ValueError("Nombre inválido")

        if not isinstance(precio, (int, float)):
            raise ValueError("Precio inválido")

        self.nombre = nombre
        self.precio = precio
