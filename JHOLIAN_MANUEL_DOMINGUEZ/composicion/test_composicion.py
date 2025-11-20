from composicion import Persona, Corazon

def test_instancia_corazon():
    corazon = Corazon()
    assert isinstance(corazon, Corazon)

def test_metodo_corazon():
    corazon = Corazon()
    assert corazon.latir() == "latido"

def test_persona_tiene_corazon_en_constructor():
    persona = Persona()
    assert isinstance(persona.corazon, Corazon)

def test_persona_metodo():
    persona = Persona()
    assert persona.sentir_latido() == "latido"
