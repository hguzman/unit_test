class Llanta:
    def __init__(self, tamaño, tipo):
        self.tamaño = tamaño
        self.tipo = tipo


class Carro:
    def __init__(self, modelo: str, marca: str, ano: int):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.llantas = []

    def agregar_llanta(self, llanta):
        if not isinstance(llanta, Llanta):
            raise TypeError("Solo puedes agregar de tipo Llanta")
        self.llantas.append(llanta)
