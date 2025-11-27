class Pantalla:
    def __init__(self, tamaño=16, tipo="AMOLED"):
        if not isinstance(tamaño, int) or tamaño <= 10:
            raise ValueError("tamaño incorrecto")
        if not isinstance(tipo, str):
            raise ValueError("tipo incorrecto")

        self.tamaño = tamaño
        self.tipo = tipo
