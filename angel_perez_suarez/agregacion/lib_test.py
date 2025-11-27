import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from biblioteca import Biblioteca
from libro import Libro

# --------------------
# Test de instancia
# --------------------
def test_instancia_biblioteca():
    biblioteca = Biblioteca("Biblioteca Central")
    libro = Libro("Cien años de soledad", "Gabriel García Márquez")
    # Verifica que se crearon correctamente las instancias
    assert isinstance(biblioteca, Biblioteca)
    assert isinstance(libro, Libro)

# --------------------
# Test de atributos
# --------------------
def test_atributos_libro():
    libro = Libro("Don Quijote", "Miguel de Cervantes")
    assert libro.titulo == "Don Quijote"
    assert libro.autor == "Miguel de Cervantes"

# --------------------
# Test de métodos
# --------------------
def test_agregar_y_mostrar_libros():
    biblioteca = Biblioteca("Biblioteca Central")
    
    assert biblioteca is not None
    assert biblioteca.nombre == "Biblioteca Central"

    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez")
    libro2 = Libro("Don Quijote", "Miguel de Cervantes")

    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)

    lista_libros = biblioteca.mostrar_libros()
    assert "'Cien años de soledad' de Gabriel García Márquez" in lista_libros
    assert "'Don Quijote' de Miguel de Cervantes" in lista_libros
