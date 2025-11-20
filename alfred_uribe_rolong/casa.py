class Habitacion:
    def __init__(self, nombre, metros):
        self.nombre = nombre
        self.metros = metros

class Casa:
    def __init__(self, direccion):
        self.direccion = direccion
        self.habitaciones = []

    def habitacion(self, nombre, metros):
        hab = Habitacion(nombre, metros)
        self.habitaciones.append(hab)
