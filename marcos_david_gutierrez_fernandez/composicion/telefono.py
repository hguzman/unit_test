from pantalla import Pantalla

class Telefono:
    def __init__(self, numero, tipo):
        self.numero = numero
        self.tipo = tipo
    
    def agregar_pantalla(self, pantalla):
        if not isinstance(pantalla, Pantalla):
            raise ValueError("Pantalla inválida")
        self.pantalla = pantalla

    
