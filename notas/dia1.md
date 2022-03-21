# Python

Lenguaje de programación:
- Tipado dinámico (vs tipado estático):
    Al definir una varible hay que asignarle un tipo.
- Interpretado
    Que no se compila. 
    Python: Tratamiento de datos: Data mining, machine learning, deep learning
    Necesitamos un interprete:
        Cual? HAY MUCHOS interpretes de python
        Cython (el más utilizado)
            Solo permite el uso de un core
        PyPy
        Jython
- Paradigma de programación
    - Programación imperativa:
        El suministro de órdenes al intérprete secuenciales
            control de flujo: if
            bucles: for, while
    - Programación procedural:
        Crear funciones/procedimientos reutilizables  
            Procedimiento: Es un trozo de código parametrizable que se ejecuta
            Función: Es un trozo de código parametrizable que se ejecuta y devuelve algo
    - Programación funcional:
        Poder referenciar a una función desde una variable:
            Esto implica que una función puede recibir como argumentos otras funciones... incluso devolver una función
    - Programación Orientada a Objetos
        Capacidad de definir mis propios tipos de datos... que además albergan funciones propias... herencia, polimorfismo


## Variable

Es una referencia a una posición de memoria RAM en la que guardamos algo.

numero=17

17      - Pon el 17 en memoria
numero  - Crea una variable con el nombre numero
=       - Asigna la variable a eso que acabas de poner en la RAM

numero=22
22      - Pon el 22 en memoria en otro sitio
¿Cuantas cosas hay en memoria? 2
    17 y 22
numero= - Mueve el postit para pegoarlo al lado del 22.
    
    
# Funciones sobre colecciones:

## map(funcion,coleccion)

Devuelve un objeto del mismo tipo que el suministrado (coleccion)
Donde cada valor del objeto es el resultado de aplicar la función suministrada sobre cada uno de los items

(a,b,c)-> map(funcion) -> (funcion(a), funcion(b), funcion(c))

## filter(funcion,coleccion)

Dada una función que devuelve True o False, genera una coleccion que contiene los elementos de la coleccion suministrada
para los que la función devuelve True

(a,b,c) -> filter(funcion)-> (funcion(a), funcion(b), funcion(c))
                             ( True,       False    ,  False) &
                             ( a  ,         b      , c    )
                             (a,)
                             
                             
# Programación concurrente

Concurrencia: Trabajos en paralelo, que pueden ejercer influencia sobre los mismos datos.

Hilo

# Hilo (Thread) vs Proceso (Process)

# Un proceso?

Una copia de un programa cargada en memoria RAM, en ejecución                 (un estado compatible con ejecución).
- El código va a la memoria RAM
- En la ram se crean estructuras adicionales/ reserva de espacio adicional en la RAM
    - Zona prereservada donde ir almacenando los datos que va generando el programa: HEAP (entre otros la cache)
    - METHOD STACK -> suele tener un tamaño determiado y preestablecido... y a veces se llena....
        stackoverflow: Desbordamiento de pila

Stack? Pila
Estructura de datos. Equivalente a una lista, un diccionario.
Stack: Sigue un modelo LastInFirstOut

Cola: Sigue un modelo FIFO

Codigo
    funcion1
    funcion2
    funcion3
    codigo 

Quién ejecuta el código de un proceso? UN HILO !!

Contar del 1 al 10

Puedo tener un programa que ejecute 2 hilos                         -> El programa está en RAM 1 vez
                                                                        Solo hay una HEAP compartida por los hilos
Puedo tener 2 procesos, cada uno con su hilo, ejecutando un programa-> El programa está 2 veces en RAM
                                                                        Cada hilo tiene su HEAP


Cuando quiero que un programa abra uun nuevo hilo de ejecución paralela... 
lo que necesito es a ese nuevo hilo, darle un cometido: función
