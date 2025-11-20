import pytest
from pantalla import Pantalla
from telefono import Telefono

def test_pantalla_valida():
    p = Pantalla(15, "OLED")
    assert p.tamaño == 15
    assert p.tipo == "OLED"

def test_pantalla_tamaño_invalido():
    with pytest.raises(ValueError):
        Pantalla(5, "LCD")

def test_pantalla_tipo_invalido():
    with pytest.raises(ValueError):
        Pantalla(12, 123)

def test_agregar_pantalla_valida():
    t = Telefono("123456789", "Smartphone")
    p = Pantalla(16, "AMOLED")
    t.agregar_pantalla(p)
    assert t.pantalla == p



