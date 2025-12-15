from Avion import avion, aeropuerto


def test_instancia_avion_aeropuerto():
    a1 = avion("Boeing 737", 180, 850)
    aerop = aeropuerto("Barajas", "Madrid")

    assert isinstance(a1, avion)
    assert isinstance(aerop, aeropuerto)


def test_atributos_avion():
    a1 = avion("Airbus A320", 150, 830)

    assert a1.modelo == "Airbus A320"
    assert a1.capacidad == 150
    assert a1.velocidad == 830


def test_agregar_avion():
    assert len(aerop.aviones) == 0
    
    a1 = avion("Boeing 737", 180, 850)
    aerop = aeropuerto("Barajas", "Madrid")

    

    aerop.agregar_avion(a1)

    assert len(aerop.aviones) == 1
    assert a1 in aerop.aviones
