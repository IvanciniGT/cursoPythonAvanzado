def funcion1(argumento1):
    print(argumento1)

funcion1("Ivan")

variable_que_referencia_a_una_funcion=funcion1

variable_que_referencia_a_una_funcion("Lucas")

##################################

def saludo(nombre):
    return "Hola "+ nombre
    
def despedida(nombre):
    return "Adios "+ nombre

### Programación funcional
def imprimir(funcion_composicion_saludo, nombre):
    print(funcion_composicion_saludo(nombre))
imprimir(saludo,"iván")
### Programación procedural
def imprime(texto):
    print(texto)
imprime(saludo("iván"))
###

# Capacidad de definir funciones anónimas: LAMBDA EXPRESSIONS

imprimir(lambda nombre: "HOLA "+ nombre+"!"*27 ,"iván")

lista=(1,2,3,4,5)

triple_de_los_valores=map(lambda numero: numero*3, lista)
for valor in triple_de_los_valores:
    print(valor)
    
lista=("Iván", " Lucas", "Concha ")

nombres_convertidos= map(lambda nombre: nombre.strip(), map(lambda nombre: nombre.upper(), lista))
for valor in nombres_convertidos:
    print(valor)



lista=(1,2,3,4,5,6,7,8,9,10)


# Programación funcional
lista_pares= filter(lambda numero: True if numero%2==0 else False, lista)
# programación imperativa
lista_pares=[]
for numero in lista:
    if numero%2==0:
        lista_pares.append(numero)
###
for valor in lista_pares:
    print(valor)
    

# Estrategia Recursiva
def factorial(numero):
    if numero==0:
        return 1
    return numero*factorial(numero-1)    
    
print(factorial(5))

# 5! = 5x4x3x2x1 = 120
# 4! = 4x3x2x1   = 24
# n! = n x (n-1)!
#   0! = 1

# Que hace el hilo que ejecuta el programa
#   LINEA
#   67      -> factorial(5) .... esa linea de código se quede en pausa
#   62      -> numero=5     63(salta)->65 -> factorial(4) .... se queda en pausa
#   62.     -> numero=4     63(salta)-> 65  -> factorial(3)... se queda en pausa
#   62.     -> numero=3     63(salta)-> 65  -> factorial(2)... se queda en pausa
#   62.     -> numero=2     63(salta)-> 65  -> factorial(1)... se queda en pausa
#   62.     -> numero=1     63(salta)-> 65  -> 1*1=1
import time 
from threading import Thread

    
def contar(nombre,maximo,siesta):
    for numero in range(1, maximo+1):
        print("soy el contador: "+nombre+". Voy por el numero: " + str(numero))
        time.sleep(siesta) # Esto se lo digo a quién?

hilo_paralelo=Thread(  target= lambda: contar("A",10, 1)   )
hilo_paralelo.start()
contar("B",6, 2)
# main y hilo_paralelo
