from enum import Enum

class Estado(Enum):
    PENDIENTE = 0
    RESUELTA_CORRECTAMENTE = 1
    RESUELTA_CON_ERROR = 2

class Promesa:
    
    def __init__(self):
        self.estado=Estado.PENDIENTE
        self.error=None
        self.valor=None
