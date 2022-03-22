
from servicio import Servicio
class Servidor:
    
    # Constructor
    def __init__(self, nombre, ips=[], servicio: Servicio = None):
        self.nombre=nombre
        self.ips=ips
        self.servicio=servicio

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self,nuevoNombre):
        self._nombre=nuevoNombre.lower()

    def __str__(self):
        return "Servidor: "+self._nombre
        