import pytest
from casa import Casa, Habitacion
from carro import Carro, Llanta

#compocicion

def test_instancia_casa():
    casa = Casa("Calle 123")
    assert isinstance(casa, Casa)


def test_agregar_habitacion():
    casa = Casa("Calle 123")
    casa.habitacion("Sala", 25)
    
    assert len(casa.habitaciones) == 1
    assert casa.habitaciones[0].nombre == "Sala"
    assert casa.habitaciones[0].metros == 25


def test_atributo_habitacion():
    hab = Habitacion("Dormitorio", 12)
    assert hab.nombre == "Dormitorio"
    assert hab.metros == 12

#agregacion

def test_atributo():
    carro = Carro("Mazda 3")
    assert carro.modelo == "Mazda 3"


def test_agregar_llantas():
    carro = Carro("Mazda 3")
    l1 = Llanta("20 pulgadas", "deportiva")
    l2 = Llanta("20 pulgadas", "deportiva")

    carro.agregar_llanta(l1)
    carro.agregar_llanta(l2)

    assert len(carro.llantas) == 2
    assert carro.llantas[0].tamaño == "20 pulgadas"


def test_instancia():
    carro = Carro("Mazda 3")
    assert isinstance(carro, Carro)
    with pytest.raises(TypeError):
        carro.agregar_llanta("esto no es una llanta")



