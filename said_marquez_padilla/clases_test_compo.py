class Celular:
    def __init__ (self, marca, modelo):
        self.modelo = modelo
        self.marca = marca
        self.camara_principal = Camara("principal", 108)
        self.camara_ultra = Camara("ultra angular", 48)
        self.camara_macro = Camara("macro",5)

    def totalmegapixeles(self):
        return(self.camara_principal.megapixeles +
                self.camara_ultra.megapixeles +
                self.camara_macro.megapixeles)
    
class Camara:
    def __init__ (self,tipo,megapixeles):
        self.tipo = tipo
        self.megapixeles = megapixeles
        