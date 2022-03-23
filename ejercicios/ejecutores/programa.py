from poolejecutores import PoolEjecutores
import time
from promesa import Estado
import threading

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
    print("Trabajo concluido HILO EXTERNO   ["+str(threading.get_ident())+"]: "+ref)
    
def trabajoConcluidoHiloPrincipal(ref):
    print("Trabajo concluido HILO PRINCIPAL ["+str(threading.get_ident())+"]: "+str(ref))
    
# El hilo principal !!!
mi_pool_de_ejecutores=PoolEjecutores(5, 1)
mi_pool_de_ejecutores.start()

promesas=[]
total_trabajos=0
for numero in range(0,20):

    promesa=mi_pool_de_ejecutores.nuevoTrabajo((lambda numero: lambda: unTrabajoEstupido(numero))(numero))
    promesas.append(promesa)
    total_trabajos+=1

    promesa=mi_pool_de_ejecutores.nuevoTrabajo((lambda numero: lambda: unTrabajoMenosEstupido(numero))("B_"+str(numero)), trabajoConcluido)
    promesas.append(promesa)
    total_trabajos+=1

#time.sleep(20)
#for numero in range(0,20):
#    mi_pool_de_ejecutores.nuevoTrabajo((lambda numero: lambda: unTrabajoEstupido(numero))(numero))

while len(promesas)>0:
    for promesa in promesas:
        if promesa.estado==Estado.RESUELTA_CORRECTAMENTE:
            trabajoConcluidoHiloPrincipal(promesa.valor)
            promesas.remove(promesa)
        elif promesa.estado==Estado.RESUELTA_CON_ERROR:
            trabajoConcluidoHiloPrincipal(promesa.error)
            promesas.remove(promesa)
    
    procesados_hasta_ahora=total_trabajos-len(promesas)
    print( "X"*procesados_hasta_ahora + "·"*len(promesas) )

    time.sleep(0.5)

mi_pool_de_ejecutores.waitForPending()

# Yo quiero tener un código que se ejecute por este hilo, cuando el otro acabe su trabajo
print("Ya acabó")


# Después de que acabe de ejecutarse cada tarea estupida, quiero que se me avise... para poder hacer algo más




