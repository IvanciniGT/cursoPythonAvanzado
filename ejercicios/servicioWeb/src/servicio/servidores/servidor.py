from comun.objetopersistente import ObjetoPersistente
from servicio.inicializador import base_datos

# Clase Servidor
# Nombre
# Descripcion
# IP
# Activo

class Servidor(ObjetoPersistente,base_datos.Model):
    
    # Definiremos unas variables de CLASE.
    # Estas variables serán utilizadas por SWLAchemy para generar un modlo de BBDD adecuado (tabla) 
    # donde almacenar estos objetos
    id          = base_datos.Column(base_datos.Integer, primary_key=True)
    nombre      = base_datos.Column(base_datos.String)
    ip          = base_datos.Column(base_datos.String)
    descripcion = base_datos.Column(base_datos.String)
    estado      = base_datos.Column(base_datos.Boolean)
    
    def __init__(self, nombre, ip, descripcion=None, estado=False):
        self.nombre=nombre
        self.ip=ip
        self.descripcion = descripcion if descripcion is not None else nombre
        self.estado=estado
    
    @staticmethod
    def crearDesdeJSON(datos_servidor):
        return Servidor(datos_servidor['nombre'],
                        datos_servidor['ip'],
                        datos_servidor['descripcion'],
                        datos_servidor['estado']
                        )
    # guardar()
    # borrar()
    