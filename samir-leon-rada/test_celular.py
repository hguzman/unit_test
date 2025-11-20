from celular import Celular, Bateria

def test_instancia_bateria():
    cel = Celular("Samsung")
    assert isinstance(cel.bateria, Bateria)

def test_atributos():
    cel = Celular("Xiaomi")
    assert cel.marca == "Xiaomi"
    assert cel.bateria.capacidad == 5000

def test_metodo_capacidad():
    cel = Celular("Motorola")
    assert cel.obtener_capacidad_bateria() == 5000