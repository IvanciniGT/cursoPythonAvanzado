# comentarios

"""
Hola
Esto se ignora
por el interprete de python
"""

# Definir un texto multilinea

# Variables
numero=17
texto="""
Esta es la linea 1
Esta la linea 2
"""

# Tipos de datos
## Enteros
15
19
34
-17

## Decimales
34.5

## Lógicos
True
False

## Textos
"Hola soy un texto"
'Hola pues yo tambien'
"""
Texto linea 1
linea 2
linea 3
"""

# Tipos compuestos
## Tupla: Lista secuencial e inalterable de valores

(1,2,3,4,5,"Texto", True) # Este es inalterable

## Lista: Lista secuencial de valores
[1,2,3,4,5,"Texto", True] # Este es alterable
### Añadir nuevo, eliminar, cambiar un valor

lista=("a","b","c")
lista[1] # b
lista[-2] # b
lista[-1] # c
lista[0:2] # ("a","b") # El 2 no se incluye

lista[-2:] # ("b","c") 
lista[:-1] # ("a","b") 

## Diccionario
### Lista de valores, que no van ordenados (esto es mentira desde python 3.4)
### Pensados para trabajar recuperando cada valor mediante una clave
diccionario={'clave1': "Valor1",'clave2': 2,'clave3': True}
diccionario['clave2'] # 2

# Textos

## Un texto es una tupla de caracteres


texto1=("a","b","c")
texto2="abc"

texto2[2]
texto2[:-1]

# Sobre las tupla y su sintaxis:
numero=(1) # El interprete, interporeta que estamos usando los parentesis para indicar precedencia de operaciones.
otra_forma_de_definir=1

tupla=(1,)
tupla=(1,2,)
numero=(7+2)*4
tupla=("valor1", "valor2")
valor1,valor2=tupla
valor1,valor2=("valor1", "valor2")

# El () sirven para muchas cosas en python.... MUCHAS COSAS
## Definir tuplas
## Precedencia de operaciones: (3+5)*8 <> 3+5*8
## Ejecutar una función
## A la hora de definir una función, indicar los argumentos que debe/puede recibir

def miFuncion():
    print("Hola")
    
variable=miFuncion    
miFuncion()
variable()

# Programación imperativa
## Control de flujo:
# if CONDICION:
    # Codigo que quiero que se ejecute solo si se cumple la condicion
# CONDICION debe ser una expresión lógica: TRUE FALSE
    # Sirve para determinar si un trozo de código debe ejecutarse o no

numero=17
if numero>15:
    # hago algo asociado a que el numero sea mayor que 15
    print("HOLA, el numero es mayor que 15")
elif numero>10:
    print("HOLA, el numero es mayor que 10")
else:
    print("HOLA, el numero no es mayor que 15")

edad=22
mayor_de_edad=True if edad>=18 else False
              # Devuelve Tru si edad >= 18... en caso contrario devuelve False
              
# bucles: Para ejecutar un mismo código varias veces
numero=0
while numero<10:
    print(numero)
    numero=numero+1

# For: Ejecutar un trozo de código un determinado numero de veces preestablecido... asociado a tamaño de una lista/tupla
lista_valores=(1,3,5,"a")
for valor in lista_valores:
    print(valor)

for valor in (1,2,3,4,5,6,7,8,9,10):
    print(valor)

for valor in range(1,100):
    print(valor)

for valor in range(1,100,2):
    print(valor)

for valor in range(100,1,-1):
    print(valor)


# Dentro de un bucle hay 2 palabras que podemos usar:
# continue: Dejar de ejecutar la iteración actual del bucle y pasa al siguiiente valor
# break: Salir del bucle... rompe el bucle

numero=0
while numero<10:
    numero=numero+1
    if numero % 2 == 0: # Si el numero es par 
        continue        # pasa al siguiente numero
    if numero == 7:
        break
    print(numero)

print("El 7 ya no ha salido por pantalla")

# Que se puede usar en sangrado en python?
## Lo que quiera.. A python le da igual. Lo importante es mantener coherencia en cada nivel
if numero>7:
 print("hola")
 print("adios")

elif numero>20:
    print("hola2")
    print("adios3")

else:
                                    print("hola2")
                                    print("adios3")

# Operadores:
## Numericos:
### Matemáticos:
    # + - * /                                           7/3: = 2.3333333333333
    # //  División entera                               7//3 = 2
    # %   MODULO: Resto de la división entera           7#2 = 1
    
### Asignación
    # =
    # +=
    # -=
    # *=
    # /=
    
numero=8
numero+=1 # numero=numero+1
 # numero=9

### Relacionales: Devuelven un valor lógico: True-False
    # > < >= <=
    # == 
    # !=
### Operadores lógicos: Devuelven un avlor lógico, pero sus operandos son también valores lógicos
    # and
    # or
    # not
### Operadores sobre textos
    # + : CONCATENAR
"hola" +" ivan" # "hola ivan"
    # * : Replicar texto
"hola"*3    # "holaholahola"


# Funciones conversion de datos
str(32)
int("32")
float("32")
bool("True")


edad=43
nombre="Ivan"
print(nombre+" tiene "+ str(edad) +" años")
     #Ivan tiene 43 años
     
# En python hay un concepto que se denomina list comprehension:
# Recorrer una lista para dar lugar a otra lista
lista=(1,2,3,4,5)
doble_lista=[ valor * 3 if valor%2==0 else valor*2 for valor in lista ]

for valor in doble_lista:
    print(valor)

# Martin Fowler

# ADA:

## Un programa se escribe una vez, se modifica varias y se lee muchas veces. 
#
flag=True
n=17
numero_de_item_del_carro=19

# SonarQube: Analisis estático de código

# Programación procedural

#def nombreFuncion( argumentos ):
    # Codigo
    
# Una vez que pongo un valor por defecto a un parametro, ya TODOS LOS PARAMETROS SIGUIENTES DEBENE TENER VALOR POR DEFECTO 
def saluda(nombre="amig@",efusivo=True):
    if not efusivo:
        print("hola "+nombre)
    else:
        print("HOOOLAAA "+nombre +"!!!!!!!!")

saluda()
saluda("Ivan")
saluda("Menchu", True)
saluda("Lucas", )
saluda(efusivo=False)

# Una función puede devolver un valor. 
# return <VALOR>

def doble(numero):
    return numero*2
    
numero=6
doble_del_numero=doble(numero)
print(doble_del_numero)

def generar_saludo(nombre="amig@",efusivo=True):
    if not efusivo:
        return "hola "+nombre
    else:
        return "HOOOLAAA "+nombre +"!!!!!!!!"

el_saludo=generar_saludo("Ivan", True)
print(el_saludo)

def generar_saludo_2(nombre="amig@",efusivo=True):
    saludo_generado=''
    if not efusivo:
        saludo_generado= True
    else:
        saludo_generado= "HOOOLAAA "+nombre +"!!!!!!!!"
    return saludo_generado

def doble_y_triple(numero):
    return (numero*2, numero*3)

el_doble,_ =doble_y_triple(8)
print(el_doble)


resultado=doble_y_triple(8)
print( resultado[0] )
print( resultado[1] )

