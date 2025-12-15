class Motor:
    def __init__(self, potencia):
        self.potencia = potencia
        self.encendido = False


    def encender(self):
        self.encendido = True

# esoto es para apagar el carro
    def apagar(self):
        self.encendido = False
