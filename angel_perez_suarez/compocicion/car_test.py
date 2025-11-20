import sys
import os

# Agregamos la carpeta src al PATH si tus archivos están allí
sys.path.append(os.path.abspath("src"))

from carro import Coche
from motor import Motor  


# --------------------
# Test de instancia
# --------------------
def test_instancia_coche():
    coche = Coche("Toyota", 120)
    # Verifica que se creó la instancia correctamente
    assert isinstance(coche, Coche)
    # Verifica que el coche tiene un motor (composición)
    assert isinstance(coche.motor, Motor)


# --------------------
# Test de atributos
# --------------------
def test_atributos_coche():
    coche = Coche("Honda", 150)
    assert coche.marca == "Honda"
    assert coche.motor.potencia == 150


# --------------------
# Test de métodos
# --------------------
def test_arrancar_coche():
    coche = Coche("Toyota", 120)
    coche.arrancar()
    assert coche.esta_encendido() is True


def test_apagar_coche():
    coche = Coche("Toyota", 120)
    coche.arrancar()
    coche.apagar()
    assert coche.esta_encendido() is False
