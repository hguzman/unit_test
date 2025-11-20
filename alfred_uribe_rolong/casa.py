class Habitacion:
    def __init__(self, nombre, metros):
        self.nombre = nombre
        self.metros = metros

class Casa:
    def __init__(self, direccion, habitacion:Habitacion):
        self.direccion = direccion
        self.habitacion = habitacion