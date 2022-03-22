from servidor import Servidor
from servicio import Servicio
from servicio import ServicioBBDD


servidor_web=Servidor(  'web.PRODUCCION.es', 
                        ['172.17.0.2'], 
                        Servicio( 'web', [80],  'http' )
                     )
                     
servidor_bbdd=Servidor(  'bbdd.PRODUCCION.es', 
                        ['172.17.0.3'], 
                        ServicioBBDD( 'bbdd', [3306],  'mariadb', 'produccion', 'usuario_bbdd', 'password' )
                     ) 

print(servidor_web.servicio.__dict__)
print(servidor_bbdd.servicio.__dict__)



servidor_web_malo=Servidor(  'web.malo.es', 
                        ['172.17.0.3'], 
                        17
                     )
print(servidor_web_malo.__dict__)

# mariadb
#   BBDD: produccion
#   usuario: usuario_bbdd
#   contraseña: password