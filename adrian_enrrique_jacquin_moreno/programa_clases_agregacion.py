class App:
    def __init__(self, nombre, descarga):
        self.nombre = nombre
        self.descarga = descarga

class Tablet:
    apps = []
    def instalar(self, app):
        Tablet.apps.append(app)
