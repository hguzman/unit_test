from clases_test import Biblioteca, Libro
from clases_test_compo import Celular, Camara
import pytest


# Agregacion
def test_estainstancia_libro():
    libro = Libro("El principuto", "Antoine de Saint-Exupéry", 1943)
    assert isinstance(libro,Libro)

def test_estainstancia_biblioteca():
    biblioteca = Biblioteca("El panorama")
    assert isinstance(biblioteca,Biblioteca)
    

def test_atributos_libro():
    libro = Libro("1984", "Jacki el pro", 1949)
    assert libro.titulo == "1984"
    assert libro.autor == "Jacki el pro"
    assert libro.fecha_publicacion == 1949

def test_atributos_biblioteca():
    biblioteca = Biblioteca("Biblioteca nacional")
    assert biblioteca.nombre == "Biblioteca nacional"


def test_agregar_libro():
    biblioteca = Biblioteca("La Gran Mundo")
    libro1 = Libro("Cien años de soledad", "Garcia Marquez", 1967)
    libro2 = Libro("Cronica de una muerte anunciada", "Garcia Marquez", 1981)

    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)

    assert len(biblioteca.libros) == 2
    
# Composicion

def test_instancia_celular():
    celular = Celular("Samsung", "S25 Ultra")
    assert isinstance(celular,Celular)

def test_instancia_camara():
    celular19 = Celular("Samsung", "J2 Prime")
    assert isinstance(celular19.camara_principal, Camara)
    assert isinstance(celular19.camara_ultra, Camara)
    assert isinstance(celular19.camara_macro, Camara)


def test_atributo_celular():
    celular = Celular("Apple", "Iphone 16 pro max")
    assert celular.marca == "Apple"
    assert celular.modelo == "Iphone 16 pro max"


def test_metodo_megapixeles():
    celular = Celular("OnePlus", "13 Pro")
    assert celular.totalmegapixeles() == 161
