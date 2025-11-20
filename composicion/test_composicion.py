from composicion import Corazon, Persona


def test_corazon():
    c = Corazon()

    assert isinstance(c, Corazon)
    assert c.latir() == "latido"


def test_persona():
    p = Persona("Ana")

    assert isinstance(p, Persona)
    assert isinstance(p.corazon, Corazon)

    assert p.nombre == "Ana"

    assert p.latir() == "latido"