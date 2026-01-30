class Corazon:
    def __init__(self):
        self.latidos = 0 

    def latir(self):
        self.latidos += 1
        return f"Latido número {self.latidos}"


class Persona:
    def __init__(self, nombre, corazon=None):
        if corazon is None:
            corazon = Corazon()

        self.nombre = nombre
        self.corazon = corazon 

    def latir(self):
        return self.corazon.latir()