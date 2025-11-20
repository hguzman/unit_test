class Pantalla:
    def __init__(self, tamaño, tipo):
        if not isinstance(tamaño, int) or tamaño <= 10:
            raise ValueError("Tamaño inválido")
        if not isinstance(tipo, str):
            raise ValueError("Tipo inválido")
        self.tamaño = tamaño
        self.tipo = tipo

    