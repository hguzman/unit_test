class Motor:
    def encender(self):
        return "motor encendido"


class Carro:
    def __init__(self, motor):
        self.motor = motor

    def arrancar(self):
        return self.motor.encender()
