from threading import Thread
import time

class Ejecutor (Thread):
    
    cuando_no_haya_mas_para=False
    
    def __init__(self, nombre, pool_ejecutores):
        super().__init__()
        self.nombre=nombre
        self.trabajos_pendientes=pool_ejecutores.trabajos_pendientes
        self.tiempo_espera=pool_ejecutores.tiempo_espera
        self.testigo=pool_ejecutores.testigo
        
    def run(self):
        while True:
            proximoTrabajo=None
            funcionCallback=None
            
            self.testigo.acquire()
            # Codigo conflictivo
            if len(self.trabajos_pendientes)>0:
                proximoTrabajo,funcionCallback=self.trabajos_pendientes.pop(0)
            self.testigo.release()
            
            # miro si hay algun trabajo pendiente en la cola
            if proximoTrabajo is not None:
            # Si lo hay? ejecutalo
                print("Hay "+ str(len(self.trabajos_pendientes)) +" trabajos pendientes")
                print("Soy el ejecutor "+ self.nombre +" y voy a por un trabajo")
                try:
                    valor_devuelto=proximoTrabajo()
                    if funcionCallback is not None:
                        funcionCallback(valor_devuelto)
                    print("Soy el ejecutor "+ self.nombre +" y acabo el trabajo")
                    print("Todo bien")
                except Exception as error:
                    # Código que se ejecuta si hay error
                    print("Soy el ejecutor "+ self.nombre +" y hay un problema con un trabajo " + error)
                else:
                    # Código que se ejecuta si exito, si no hay error
                    print("Todo bien")
                finally:
                    # Código que se ejecuta en cualquier caso
                    print("Trabajo procesado, bien o mal... pero procesado")
                    
            elif Ejecutor.cuando_no_haya_mas_para:
                break
            else:
                # Si no lo hay? ... 
                # tendre que esperar un POCO a ver si llega algo
                print("Ahora no hay trabajos pendientes. Espero")
                time.sleep(self.tiempo_espera)
        print("Se acabó la jornada!")
    
    @classmethod
    def noEspereisMas(cls):
        Ejecutor.cuando_no_haya_mas_para=True