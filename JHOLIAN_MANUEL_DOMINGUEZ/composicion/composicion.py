class Corazon:
    def latir(self):
        return "latido"


class Persona:
    def __init__(self):
        self.corazon = Corazon()

    def sentir_latido(self):
        return self.corazon.latir()
