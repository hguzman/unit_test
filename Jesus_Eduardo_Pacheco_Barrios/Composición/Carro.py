class Motor:
    def __init__(self, tipo):
        self.tipo = tipo

class Auto:
    def __init__(self, marca, motor: Motor):
        self.marca = marca
        self.motor = Motor("Gasolina")  

