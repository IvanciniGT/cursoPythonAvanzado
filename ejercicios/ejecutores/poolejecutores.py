from ejecutor import Ejecutor
import threading

class PoolEjecutores:
    
    def __init__(self, numero_ejecutores, tiempo_espera):
        self.numero_ejecutores=numero_ejecutores
        self.tiempo_espera=tiempo_espera
        self.lista_ejecutors=[]
        self.trabajos_pendientes=[]
        self.testigo=None
    
    def start(self):
        # Crear el testigo
        self.testigo=threading.Semaphore()
        # Crear los ejecutores
        for indice in range(0,self.numero_ejecutores):
            self.lista_ejecutors.append( Ejecutor(str(indice),self) )
            self.lista_ejecutors[-1].start()
            
    def nuevoTrabajo(self, trabajo, callback=None):
        self.trabajos_pendientes.append( (trabajo,callback) )

    def waitForPending(self):
        Ejecutor.noEspereisMas()
        for ejecutor in self.lista_ejecutors:
            ejecutor.join()
        