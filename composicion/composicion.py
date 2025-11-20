class Corazon:
    def latir(self):
        return "latido"


class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.corazon = Corazon() 

    def latir(self):
        return self.corazon.latir()




    
        

