
"""
servidor_web={
    'nombre': 'web.produccion.es',
    'ips': ['172.17.0.2'],
    'servicios':[
        { 'nombre': 'web', 'puertos': [80], 'protocolo': 'http' },
        { 'nombre': 'web_segura', 'puertos': [443], 'protocolo': 'https' }
    ]
}

print(servidor_web['nombre'])
print(servidor_web['ips'])
print(servidor_web['servicios'])

servidor_base_datos={
    'nombre': 'bbdd.produccion.es',
    'ips': ['172.17.0.3'],
    'servicitos':[
        { 'nombre': 'bbdd', 'puertos': [3306], 'protocolo': 'mariadb' }
    ]
}

print(servidor_base_datos['servicitos'])

"""

# Una clase es un tipo de datos nuevo
class Servidor:
    
    # Constructor
    # Función que indica a python cómo crear nuevos datos de este nuevo tipo de datos que estamos definiendo
    def __init__(self, nombre, ips=[], servicio=None):
        self.nombre=nombre
        self.ips=ips
        self.servicio=servicio
        self._largoNombre=len(nombre)
    
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self,nuevoNombre):
        self._nombre=nuevoNombre.lower()
        self._largoNombre=len(nuevoNombre)
        
    @property
    def largoNombre(self):
        return self._largoNombre
        
    @largoNombre.setter
    def largoNombre(self, nuevoValorLargoProperty):
        print("Hola... Mi largo ahora es"+ str(nuevoValorLargoProperty))
    
    def __str__(self):
        return "Servidor: "+self._nombre
        
        
# Una clase es un tipo de datos nuevo
class Servicio:
    
    # Constructor
    # Función que indica a python cómo crear nuevos datos de este nuevo tipo de datos que estamos definiendo
    def __init__(self, nombre, puertos, protocolo):
        self.nombre=nombre
        self.puertos=puertos
        self.protocolo=protocolo

numero=17    #int(17)
texto='hola' #str('hola')
servidor_web=Servidor(  'web.PRODUCCION.es', 
                        ['172.17.0.2'], 
                        Servicio( 'web', [80],  'http' )
                     )
                     
servidor_bbdd=Servidor(  'bbdd.PRODUCCION.es', 
                        ['172.17.0.3'], 
                        Servicio( 'bbdd', [3306],  'mariadb' )
                     ) 
                     
servidor_bbdd_2=Servidor(  'bbdd2.PRODUCCION.es' ) 
                
                
                     
print(servidor_web.nombre)
print(servidor_web.ips)
print(servidor_web.servicio)
print(servidor_web.__dict__)
print(servidor_bbdd.__dict__['_nombre'])

servidor_web.nombre='web.DESARROLLO.es' # Esto el dia de mañana podría hacer que internamente llamase a una función que verificase/transformase el dato que se recibe

print(servidor_web.nombre)
print(servidor_web.largoNombre)
print(servidor_web.__dict__)

texto='hola'

print(texto)
texto.upper()
texto.lower()
texto.strip()
print(servidor_bbdd.servicio.puertos)

servidor_web.largoNombre=117


print(servidor_bbdd_2.nombre)
print(servidor_bbdd_2.ips)
print(servidor_bbdd_2.servicio)


print(str(servidor_web))
print(servidor_web.servicio)
