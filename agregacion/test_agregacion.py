from agregacion import Carro, Motor



def test_motor():
    m = Motor(100)
    assert m.potencia == 100
    assert m.encender() == "Motor encendido"


def test_carro():
    m = Motor(120)
    c = Carro("Mazda", m)

    assert c.marca == "Mazda"
    assert c.motor is m
    assert c.info() == "Carro Mazda con motor de 120 HP"
    assert c.encender_carro() == "Motor encendido"