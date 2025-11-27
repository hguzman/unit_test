import pytest
from pantalla import Pantalla
from telefono import Telefono

def test_pantalla_valida():
    p = Pantalla(15, "OLED")
    assert p.tamaño == 15
    assert p.tipo == "OLED"

def test_pantalla_tamaño_invalido():
    with pytest.raises(ValueError) as mensajeError:
        Pantalla(5, "LCD")
    assert str(mensajeError.value) == "tamaño incorrecto"

def test_pantalla_tipo_invalido():
    with pytest.raises(ValueError) as mensajeError:
        Pantalla(12, 123)
    assert str(mensajeError.value) == "tipo incorrecto"
    
def test_crear_telefono_con_pantalla():
    t = Telefono("123456789", "Smartphone", 16, "AMOLED")
    assert isinstance(t.pantalla, Pantalla)
    assert t.pantalla.tamaño == 16
    assert t.pantalla.tipo == "AMOLED"
