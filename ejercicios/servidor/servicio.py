class Servicio:
    
    # Constructor
    def __init__(self, nombre, puertos, protocolo):
        self.nombre=nombre
        self.puertos=puertos
        self.protocolo=protocolo

    def __str__(self):
        return "Servicio: "+self.nombre
        
        
class ServicioBBDD(Servicio):
    
    # Constructor
    def __init__(self, nombre, puertos, protocolo, nombre_bbdd, usuario, password):
        # Primero llama al contructor del padre(Servicio)
        super().__init__(nombre, puertos, protocolo)
        self.nombre_bbdd=nombre_bbdd
        self.usuario=usuario
        self.password=password
