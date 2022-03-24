from servicio import montarServidorFlask
from configuracion import test

config=test # TODO: Cargar configuracion de env
servidor_flask=montarServidorFlask(config)