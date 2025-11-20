###composicion 

class Motor:
    def __init__(self,numero):
        self.numero=numero


class Carro:
    def __init__(self, motor,llanta,color,placa):
        if isinstance(motor,Motor):
            self.motor=motor
        self.llanta=llanta
        self.color=color
        self.placa=placa

    def ruidoMotor(self,sonido):
        self.sonido=sonido
        return sonido



###agregacion

class Estudiante:
    def __init__(self,nombre):
        self.nombre=nombre


class Salon:
    def __init__(self,grado,colegio):
        self.grado=grado
        self.colegio=colegio
        self.estudiantes=[]
        
    def agregarEstudiantes(self,estudiante):
        if isinstance(estudiante,Estudiante):
            self.estudiantes.append(estudiante)
            



