from threading import Thread
import time

class Ejecutor (Thread):
    
    def __init__(self, nombre, trabajos_pendientes,tiempo_espera):
        super().__init__()
        self.nombre=nombre
        self.trabajos_pendientes=trabajos_pendientes
        self.tiempo_espera=tiempo_espera
        
    def run(self):
        while True:
            # miro si hay algun trabajo pendiente en la cola
            if len(self.trabajos_pendientes)>0:
            # Si lo hay? ejecutalo
                print("Hay "+ str(len(self.trabajos_pendientes)) +" trabajos pendientes")
                print("Soy el ejecutor "+ self.nombre +" y voy a por un trabajo")
                self.trabajos_pendientes.pop(0)()
                print("Soy el ejecutor "+ self.nombre +" y acabo el trabajo")
            else:
                # Si no lo hay? ... 
                # tendre que esperar un POCO a ver si llega algo
                print("Ya no quedan trabajos pendientes")
                time.sleep(self.tiempo_espera)
        