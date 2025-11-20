class Biblioteca:
    def __init__ (self,nombre):
        self.nombre = nombre
        self.libros = []

    def agregar_libro(self,libro):
        if libro not in self.libros:
            self.libros.append(libro)


class Libro:
    def __init__(self,titulo,autor,fecha_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.fecha_publicacion = fecha_publicacion
