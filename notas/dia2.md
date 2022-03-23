# Orientación a objetos

Paradigma de programación.
Definimos nuestros propios tipos de datos complejos, pueden tener sus propios métodos.

Servidor:
- nombre
- ips
- servicios:
    - nombre
      puertos
      protocolo


# JAVA

class Servidor{
    
    private String nombre;
    public Array<String> ips;
    
    public Servidor(String nombre, Array<String> ips){
        this.nombre=nombre;
        this.ips=ips;
    }
    public void setNombre(String nuevoNombre){
        this.nombre=nuevoNombre;
    }
    public String getNombre(){
        return this.nombre;
    }
}

Servidor servidor_web=new Servidor("servidor.produccion.es", .... );
servidor_web.setNombre(servidor.desarrollo.es");

# Encapsulación

En python no se implementa como en otros lenguajes.


## Hilos

monitorizando unos servicios

monitorizando unas carpetas de un servidor

monitorizar unas bbdd / servidores web

200 servidores web que monitorizar:
- Petición http
- Si contesta, mirar que conteste algo coherente

Cómo nos enfrentamos a esto?
Lanzamos peticiones 1 a 1?                  Poco optimo
Lanzamos las 200 peticiones a la vez?       Saturamos la maquina/red

Quizás... a mi me interesa lanzar peticiones de 10 en 10

Cola de trabajos < pool de threads
-------------------------------------------------
                        monitorizador 1
                        monitorizador 2
Servidor 3              monitorizador 3
...                         ...
Servidor 200            monitorizador 10
Servidor 1
Servidor 2


Cola de trabajos:
    ¿Qué guardo?        trabajos: funciones
    lista = []
    
Pool de ejecutores:
    lista = []          hilos


meter cosas en una lista: lista.append(ALGO)
Sacar cosas de una lista: lista[0]
Borrar algo de la lista:  lista.remove(ALGO)

lista.pop(0): Me da el primer elemento de la lista y lo borra de la lista

1 < 2 < 3 < 4
pop         append

FIFO
    




-O--OO-O-O-OO---------------------------main
\--------------/ /   /  /
\---------------/   /  /
\------------------/  /
\--------------------/


self.trabajos_pendientes=[  ]

if len(self.trabajos_pendientes)>0:         hilo1: True     hilo2: True
                                            hilo1           
    self.trabajos_pendientes.pop(0)()       hilo1: TRABAJO1 hilo2: ERROR
    
Semaforo

2 opciones: Evitar el error
            Capturar el error *****

Exception < Impredecible: Se que puede ocurrir, pero no se cuando va a ocurrir

HILO PRINCIPAL va poniendo trabajo->
        Pool apunta trabajo y tiene su propio hilo que lo reparte Bucle
            Pool reparte trabajo HILO


testigo=threading.Semaphore()

testigo.acquire()
# Codigo
testigo.release()



pool ejecutores
    cola_trabajos_pendientes 

    ejecutores 
        ejecutor1: TRABAJO1 PUF !
        
        
        
Trabajo gordo: 10 trabajos pequeños HILOS
    Cada uno es meter algo en una BBDD
Cuando termine cada trabajo... lo mando por correo
    Tengo otro pool: 
    
    
Promesas<
A la promesa le puedo preguntar si está resuelta ya. Pido el valor.

