import pytest
from taller2 import Computadora, Componente


def test_componente_es_instancia():
    componente = Componente('GPU', 'NVIDIA')
    assert isinstance(componente, Componente)
    assert componente.tipo == 'GPU'
    assert componente.marca == 'NVIDIA'

def test_metodos_computador ():
    computador = Computadora ("Inspiron 3000", "Dell", 2020)
    assert len (computador.componentes) == 0
    componente1 = Componente('GPU', 'NVIDIA')
    computador.add_componente(componente1)
    assert len (computador.componentes) == 1

def test_atributos_computadora_y_componente():
    componente = Componente('GPU', 'NVIDIA')
    assert componente.tipo == 'GPU'
    assert componente.marca == 'NVIDIA'

    computador = Computadora("Inspiron 3000", "Dell", 2020)
    assert computador.modelo == "Inspiron 3000"
    assert computador.marca == "Dell"
    assert computador.anio == 2020
    assert computador.componentes == []
    computador.add_componente(componente)
    assert len(computador.componentes) == 1
    assert computador.componentes[0].tipo == "GPU"
    assert computador.componentes[0].marca == "NVIDIA"
