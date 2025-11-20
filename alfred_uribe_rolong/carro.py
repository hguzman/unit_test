class Llanta:
    def __init__(self, tamaño, tipo):
        self.tamaño = tamaño
        self.tipo = tipo

class Carro:
    def __init__(self, modelo):
        self.modelo = modelo
        self.llantas = []

    def agregar_llanta(self, llanta: Llanta):
        if not isinstance(llanta, Llanta):
            raise TypeError("Solo se pueden agregar objetos tipo Llanta")
        self.llantas.append(llanta)
