# Clase Servidor
# Nombre
# Descripcion
# IP
# Activo

class Servidor():
    # id
    def __init__(self, nombre, ip, descripcion=None, estado=False):
        self.id=17 # TODO: Cambiar por un id generado en BBDD
        self.nombre=nombre
        self.ip=ip
        self.descripcion = descripcion if descripcion is None else nombre
        self.estado=estado
    
    @staticmethod
    def crearDesdeJSON(datos_servidor):
        return Servidor(datos_servidor['nombre'],
                        datos_servidor['ip'],
                        datos_servidor['descripcion'],
                        datos_servidor['estado']
                        )
