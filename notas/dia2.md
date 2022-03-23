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



# Procesos

## En ocasiones quiero que se ejecuten de forma sincrona

Porque el proceso sea de diferente naturaleza (que sea otro programa diferente)

## En ocasiones quiero que se ejecuten de forma asincrona


# Podemos juntar hilos y procesos

-------main------------------------------------
            \-----Proceso sincrono--/
            \-----Proceso sincrono--/
            \-----Proceso sincrono--/
            \-----Proceso sincrono--/
            
# pip

Instalar librerias creadas por otros
Problema al usar pip e instalar librerias creadas por otros:
- Versiones

Si tengo 5 programas y cada uno requiere de una versión de la libreria

# Python 2 -> 3

Algunas funciones no se invocaban mediante el signo de parentesis

print "HOLA"    ->          print("HOLA")

## Este problema tenemos 2 formas de resolverlo:

El poder tener versiones distintas de librarias que usemos en distintos programas

### Contenedores

Entorno aislado donde ejecutar procesos dentro de un SO Linux.

Entorno aislado:
    - Su propia conf de red
    - Su propio sistema de archivos (HDD, FS)
    - Su propia conf (variables de entorno)
    - Limitación en acceso al HW del host

Docker for windows: |           (hyperv < wsl2)
Docker for mac:     | MV Linux 

Los contenedores se crean desde una imágen de contenedor. 
Las descargamos desde un registry de repositorios de imagenes de contenedor: 
- docker hub
- quay.io           < Redhat

### VirtualEnv

Entorno (carpeta) donde tengo unas librerias asociadas a ese entorno
Crear un venv
Activo o desactivo un venv


App1 + App2 + App3      Problema: dependencias incompatibles
------------------                si uno se vuelve loco: 100% CPU, RAM, IO
       SO                         seguridad
------------------
     Maquina


 App1 | App2 + App3
------------------          Cada MV tiene: 
 SO1  |  SO2                    Su propia conf de red
------------------              Su propio sistema de archivos (HDD, FS)
 MV1  |  MV2                    Su propia conf (variables de entorno)
------------------              Limitación en acceso al HW del host
    hypervisor
------------------          Problemas:
       SO                       Ineficiencia + Despercicio
------------------              Perdida de performance
     Maquina                    Follon, complejidad


 App1 | App2 + App3             Su propia conf de red
------------------              Su propio sistema de archivos (HDD, FS)
 C1   |  C2                     Su propia conf (variables de entorno)
------------------              Limitación en acceso al HW del host
Gestor de contenedores: docker + podman + crio + containerd
------------------              Estandarizado: OpenContainerInitiative (Docker)
    SO Linux             
------------------          
    Maquina                



Kernel Linux
Ubuntu:
    bash
    sh
    cd 
    cat
    tail
    touch
    apt
    apt-get

Fedora:
    bash
    sh
    cd 
    cat
    tail
    touch
    rpm
    yum
    dnf

Alpine:
    sh
    cd 
    cat
    tail
    touch

# Trabajando con docker

docker [TIPO_OBJETO] [VERBO] <args>

docker image pull python:3.6.4                      <> docker pull python:3.6.4
docker image list                                   <> docker images

docker container create --name mipython python:3.6.4
docker container list --all                         <> docker ps --all

docker start mipython
docker stop mipython

docker container rm mypython -f                       <> docker rm mipython

docker container create --name mipython -v /home/ubuntu/environment/curso:/curso python:3.6.4 sh -c "sleep 3600"

docker run:
    docker pull
    docker container create
    docker start
    docker attach               < Vincula la salida estandar del proceso principal que corre en el contenedor
                                    a mi terminal
                                 Resumiendo: Me deja ver la salida del comando de python
                                 
    docker container rm         cuando se pare, cuando acabe
    
docker run --rm -v /home/ubuntu/environment/curso:/curso python:3.6.4 python3 /curso/ejercicios/ejecutores/programa.py


# OPCION 1

Creo un contenedor que tenga dentro python... y lo arranco
    Le hago llegar mi codigo:
        - O he PREmontado un volumen                -v
        - O le copio dentro el codigo               docker cp
    Ejecuto codigo:
        docker exec miContenedorDePython python3 PROGRAMA

Entorno precreado que se mantiene entre ejecuciones

# OPCION 2

Creo un contenedor cada vez que quiera ejecutar el comando python3:
docker run --rm -v /home/ubuntu/environment/curso:/curso python:3.6.4 python3 /curso/ejercicios/ejecutores/programa.py

Entorno creado dinámicamente que se tira al acabar de ejecutar el programa

# OPCION 3

Generar una imagen de contenedor que tenga dentro mi codigo                 <<<< Puede llevar algo más de tiempo
Arrancar un nuevo contenedor que genere desde esa imagen de contenedor, con mi programa
Entorno creado dinámicamente que se tira al acabar de ejecutar el programa

Si estoy desarrollando, habitualmente opcion 1 o "2" es la que más me interesa

Cuando distribuyo, la opción 3 es la guay
