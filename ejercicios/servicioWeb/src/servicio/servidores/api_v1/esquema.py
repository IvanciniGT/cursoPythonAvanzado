from marshmallow import fields
# Vete 2 carpetas atrás y busca ahñi el archivo inicializador
# 2 carpetas porque pongo 2 puntos
# Si fuera 3 carpetas, pondría 3 puntos

from ..inicializador import ma        # Ruta relativa, referida a mi ubicación actual
#from servicio.inicializador import ma # Ruta absoluta al fichero, referida a nuestra jerarquia de modulos

# La palabra esquema hace referencia a un JSON Schema 
# {
#    'nombre': VALOR
#    'ip': VALOR
#    'descripcion': VALOR
#    'estado': VALOR
# }
class ServidorEsquema(ma.Schema):
    
    # Definimos como variables de clase las etiquetas que puedo tener el el json... junto con su tipo de datos.
    # Marshmallow hace magia, leyendo esas variable de clase y usándolas para validar un JSON
    id              = fields.Integer(dump_only=True)
    nombre          = fields.String()
    ip              = fields.String()
    descripcion     = fields.String()
    estado          = fields.Bool()
    
    # Marshmallow aplicará este esquema al leer y al generar un JSON
        #                                   load      dump
    # El campo ID solamente se usa en el JSON cuando es un JSON generado por Marshmallow..
    # En JSONs que lea Marshmallow, ahi no se leerá el campo el ID

esquema_del_servidor=ServidorEsquema()                                          # CASO 3