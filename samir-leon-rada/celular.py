class Bateria:
    def __init__(self, capacidad):
        self.capacidad = capacidad

class Celular:
    DEFAULT_BATTERY_CAPACITY = 5000
    def __init__(self, marca, bateria_capacidad=DEFAULT_BATTERY_CAPACITY):
        self.marca = marca
        self.bateria = Bateria(bateria_capacidad)

    def obtener_capacidad_bateria(self):
        return self.bateria.capacidad