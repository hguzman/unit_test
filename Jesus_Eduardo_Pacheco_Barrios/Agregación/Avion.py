class avion:
    def __init__(self, modelo, capacidad, velocidad):
        self.modelo = modelo
        self.capacidad = capacidad
        self.velocidad = velocidad

class aeropuerto:
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion

        self.aviones = []

    def agregar_avion(self, avion):
        self.aviones.append(avion)