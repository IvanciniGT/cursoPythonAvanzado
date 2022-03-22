import time 
from threading import Thread


class Contador(Thread):

    cancelarCuentas=False

    def __init__(self, nombre, maximo, siesta ):
        super().__init__()
        self.nombre=nombre
        self.maximo=maximo
        self.siesta=siesta
        self.contar=False

    def run(self):
        self.contar=True
        for numero in range(1, self.maximo+1):
            print("soy el contador: "+self.nombre+". Voy por el numero: " + str(numero))
            time.sleep(self.siesta) # Esto se lo digo a quién?
            if self.contar==False or Contador.cancelarCuentas:
                break

    def dejaDeContar(self):
        print("> Solicitada parada del contador: "+self.nombre)
        self.contar=False

    @classmethod
    def dejadDeContarTodosMalditos(cls): # cls=Contador
        print("> Solicitada parada de todos los contadores")
        cls.cancelarCuentas=True


hilo1=Contador( "A",10, 1)
hilo1.start()   # Internamente crea un hilo... y a ese hilo es al que le pide que ejecute la función run

hilo2=Contador( "B",6, 2)
hilo2.start()

hilo3=Contador( "C",500, 0.5)
hilo3.start()

# Quien lo ejecuta? El hilo __main__
print("Contando")

# Me gustaria que a los 5 segundos... el hilo principal le diera la orden al hilo1 de dejar de contar
time.sleep(5)
hilo1.dejaDeContar()
print("Paro el hilo 1: Contador A")
# A los 2 segundos quiro que paren todos los que queden.... Siendo todos ... desconocido
time.sleep(2)
Contador.dejadDeContarTodosMalditos()
print("Paro el resto de contadores")

hilo1.join() # Espera a seguir haciendo cosas... a que el hilo 1 acabe
hilo2.join() # Espera a seguir haciendo cosas... a que el hilo 1 acabe
hilo3.join() # Espera a seguir haciendo cosas... a que el hilo 1 acabe
print("Acabado!!!")


# -----------------------------------------o----o----print--------------------------------- main
#   \    \                          \     /    /
#    -----\--------Contando A -------X----    /                                             hilo 1
#          \                                 /
#           --------------Contando B --------                                               hilo 2
