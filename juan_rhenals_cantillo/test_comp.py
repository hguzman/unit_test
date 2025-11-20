from comp import Motor, VehiculoCompuesto

def test_composicion_instancias():
    coche = VehiculoCompuesto("Honda", "Civic", 2022)
    assert isinstance(coche.motor, Motor)

def test_composicion_metodo_aumentar_hp():
    coche = VehiculoCompuesto("Ford", "Fiesta", 2020)
    coche.aumentar_hp(30)
    assert coche.motor.hp == 150  

def test_composicion_atributos_motor():
    coche = VehiculoCompuesto("Nissan", "Versa", 2021)
    assert coche.motor.hp == 120
    assert coche.motor.tipo == "Gasolina"
