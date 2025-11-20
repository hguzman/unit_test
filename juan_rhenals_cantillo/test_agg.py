import pytest
from agg import Rueda,VehiculoAgregado

def test_agregacion_instancias():
    coche = VehiculoAgregado("Toyota", "Corolla", 2020)
    rueda = Rueda("15", "Normal")
    coche.add_rueda(rueda)
    assert len(coche.ruedas) == 1
    assert isinstance(coche.ruedas[0], Rueda)

def test_agregacion_metodo_add_rueda():
    coche = VehiculoAgregado("Mazda", "3", 2021)
    rueda1 = Rueda("16", "Deportiva")
    rueda2 = Rueda("16", "Deportiva")
    coche.add_rueda(rueda1)
    coche.add_rueda(rueda2)
    assert len(coche.ruedas) == 2

def test_agregacion_atributos_rueda():
    rueda = Rueda("17", "Offroad")
    assert rueda.tamano == "17"
    assert rueda.tipo == "Offroad"


    





