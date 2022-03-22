from poolejecutores import PoolEjecutores
import time

def unTrabajoEstupido(num):
    print("Empiezo el trabajo "+str(num))
    time.sleep(3)
    print("Acabo el trabajo "+str(num))

# El hilo principal !!!
mi_pool_de_ejecutores=PoolEjecutores(5, 1)
mi_pool_de_ejecutores.start()

for numero in range(0,20):
    mi_pool_de_ejecutores.nuevoTrabajo((lambda numero: lambda: unTrabajoEstupido(numero))(numero))

#time.sleep(20)
#for numero in range(0,20):
#    mi_pool_de_ejecutores.nuevoTrabajo((lambda numero: lambda: unTrabajoEstupido(numero))(numero))

mi_pool_de_ejecutores.waitForPending()
print("Ya acabó")