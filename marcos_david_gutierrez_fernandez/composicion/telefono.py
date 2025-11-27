from pantalla import Pantalla

class Telefono:
    def __init__(self, numero, tipo, tamaño_pantalla, tipo_pantalla):
        self.numero = numero
        self.tipo = tipo
        self.pantalla = Pantalla(tamaño_pantalla, tipo_pantalla)
