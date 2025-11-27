from compocicion import Corazon, Persona

def test_atributos_corazon():
    c = Corazon()
    assert c.latidos == 0


def test_atributos_persona():
    p = Persona("Carlos")
    assert p.nombre == "Carlos"
    assert isinstance(p.corazon, Corazon)
    assert p.corazon.latidos == 0


def test_metodo_latir_corazon():
    c = Corazon()
    assert c.latir() == "Latido número 1"
    assert c.latir() == "Latido número 2"


def test_metodo_latir_persona():
    p = Persona("Ana")
    mensaje = p.latir()
    assert mensaje == "Latido número 1"
    assert p.corazon.latidos == 1


def test_instancia_corazon():
    c = Corazon()
    assert isinstance(c, Corazon)


def test_instancia_persona():
    p = Persona("Luis")
    assert isinstance(p, Persona)
    assert isinstance(p.corazon, Corazon)




