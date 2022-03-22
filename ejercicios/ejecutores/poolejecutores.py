from ejecutor import Ejecutor

class PoolEjecutores:
    
    def __init__(self, numero_ejecutores, tiempo_espera):
        self.numero_ejecutores=numero_ejecutores
        self.tiempo_espera=tiempo_espera
        self.lista_ejecutors=[]
        self.trabajos_pendientes=[]
    
    def start(self):
        # Crear los ejecutores
        for indice in range(0,self.numero_ejecutores):
            self.lista_ejecutors.append( Ejecutor(str(indice),self.trabajos_pendientes,self.tiempo_espera) )
            self.lista_ejecutors[-1].start()
            
    def nuevoTrabajo(self, trabajo):
        self.trabajos_pendientes.append(trabajo)
    
    def waitForPending(self):
        