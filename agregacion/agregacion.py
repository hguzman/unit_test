class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

    def encender(self):
        return "Motor encendido"


class Carro:
    def __init__(self, marca, motor: Motor):
        self.marca = marca
        self.motor = motor

    def info(self):
        return f"Carro {self.marca} con motor de {self.motor.potencia} HP"

    def encender_carro(self):
        return self.motor.encender()

