from composicion import Corazon, Persona


def test_atributos_corazon():
    assert Corazon().latidos == 0


def test_atributos_persona():
    p = Persona("Carlos")
    assert p.nombre == "Carlos"
    assert isinstance(p.corazon, Corazon)
    assert p.corazon.latidos == 0


def test_metodo_latir_corazon():

    assert Corazon().latir() == "Latido número 1"

    assert Corazon().latir() == "Latido número 1"


def test_metodo_latir_persona():
    p = Persona("Ana")
    mensaje = p.latir()
    assert mensaje == "Latido número 1"
    assert p.corazon.latidos == 1


def test_instancia_corazon():
    assert isinstance(Corazon(), Corazon)


def test_instancia_persona():
    p = Persona("Luis")
    assert isinstance(p, Persona)
    assert isinstance(p.corazon, Corazon)
    assert p.corazon.latidos == 0


def test_persona_con_corazon_externo():

    persona = Persona("Mario", Corazon())

    assert isinstance(persona.corazon, Corazon)
    assert persona.corazon.latidos == 0

    persona.latir()

    assert persona.corazon.latidos == 1
