# Esto nos permite crear servicios REST
from flask_restful import Resource

# Esto nos permite acceder a los datos que me manden en una petición(request)
from flask import request

# Importamos los esquemas para lvalidar/generar los JSON
from esquema import esquema_del_servidor                                            # CASO 3
# from esquemas import ServidorEsquema                                              # CASO 1 y CASO 2
# El caso1, me permitiría usar esta instancia en otras clases o codigos que crease
# esquema_del_servidor=ServidorEsquema()                                            # CASO 2

from .servidor import Servidor
# from servicio.servidores.servidor import Servidor                                 # Alternativa de importación

class RecursoServidores(Resource):
    
    # esquema_del_servidor=ServidorEsquema()                                        # CASO 1
    
    def get(self):
        codigo_respuesta=200
        json_a_devolver='{}'
        # Recuperar los servidores (todos) BBDD
        # Convertirlos a json
        return json_a_devolver, codigo_respuesta
    
    def post(self):
        codigo_respuesta=201
        json_a_devolver='{}'
        # Los datos del nuevo servidor me los mandan en un JSON,
        datos_recibidos=request.get_json()
        
        # Filtrarlo/Validarlo de acuerdo al esquema ServidorEsquema
        datos_servidor=esquema_del_servidor.load(datos_recibidos)                   # CASO 2 y CASO 3
        # RecursoServidores.esquema_del_servidor.load(datos_recibidos)              # CASO 1
        
        # Crear un objeto de tipo Servidor
        nuevo_servidor=Servidor.crearDesdeJSON(datos_servidor)

        # TODO: Crear un objeto de tipo Servidor -> BBDD
        json_a_devolver = esquema_del_servidor.dump(nuevo_servidor)
        return json_a_devolver, codigo_respuesta
    