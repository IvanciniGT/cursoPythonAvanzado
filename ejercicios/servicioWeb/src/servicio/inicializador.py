from flask_marshmallow import Marshmallow
# Solo queremos un iobjeto de tipo Marshamallow... independientemente de la cantidad de esquemas que defina
ma = Marshmallow()

from flask_sqlalchemy import SQLAlchemy
base_datos=SQLAlchemy()

from flask import Blueprint
api_servicio_blueprint=Blueprint('api_servicio',__name__)

# Este es el que crea/mantiene la estructura de BBDD
from flask_migrate import Migrate
gestor_estructura_base_datos=Migrate()
