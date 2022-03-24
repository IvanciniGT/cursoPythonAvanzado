from flask import Flask
from .inicializador import ma, base_datos
from .inicializador import api_servicio_blueprint, gestor_estructura_base_datos

def montarServidorFlask(configuracion):
    app=Flask(__name__) # el servidor lo inicializo con un nombre... el del modulo
    # Configurar el servidor de flask
    app.config.from_object(configuracion)
    
    # Necesito configurar y arrancar las extensiones
    ma.init_app(app)
    base_datos.init_app(app)
    gestor_estructura_base_datos.init_app(app)
    
    # Enchufarle la API
    app.register_blueprint(api_servicio_blueprint)
    return app