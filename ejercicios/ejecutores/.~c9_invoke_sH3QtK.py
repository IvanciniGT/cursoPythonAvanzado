from poolejecutores import PoolEjecutores
import time

def unTrabajoEstupido(num):
    print("Empiezo el trabajo "+str(num))
    time.sleep(3)
    print("Acabo el trabajo "+str(num))
    num=3/0

def unTrabajoMenosEstupido(num):
    print("Empiezo el trabajo menos estupido "+str(num))
    time.sleep(2)
    print("Acabo el trabajo menos estupido "+str(num))
    return num

def trabajoConcluido(ref):
    print("Trabajo concluido: "+ref)
    
# El hilo principal !!!
mi_pool_de_ejecutores=PoolEjecutores(5, 1)
mi_pool_de_ejecutores.start()

for numero in range(0,20):
    mi_pool_de_ejecutores.nuevoTrabajo((lambda numero: lambda: unTrabajoEstupido(numero))(numero))
    mi_pool_de_ejecutores.nuevoTrabajo((lambda numero: lambda: unTrabajoMenosEstupido(numero))("B_"+str(numero)), trabajoConcluido)

#time.sleep(20)
#for numero in range(0,20):
#    mi_pool_de_ejecutores.nuevoTrabajo((lambda numero: lambda: unTrabajoEstupido(numero))(numero))

mi_pool_de_ejecutores.waitForPending()

# Yo quiero tener un código que se ejecute por este hilo, cuando el otro acabe su trabajo
print("Ya acabó")


# Después de que acabe de ejecutarse cada tarea estupida, quiero que se me avise... para poder hacer algo más




