# Crear una imagen de contenedor

docker build -f contenedor/Dockerfile .

docker build --build-arg CARPETA=/appo -f contenedor/Dockerfile -t miapp:1.0.0 . && docker run --rm miapp:1.0.0 && docker image prune -f

docker-compose.yaml

HELM < chart
plantilla -> kubernetes-spec.yaml

## Flask

Montar una webapp... Lleva un servidor integrado

Por ejemplo, para desarrollar un api-rest

## API rest

Servicio bajo procolo http(s)

metodos:
    get
    put
    post
    patch
    delete
    head
    
Petición URL

PROTOCOLO HTTP + HTML / TCP
    URL
        request     flask.request
        genera      lee
    Cliente -> Request -> Server -> Response
                headers              headers
                    method              response_code
                body                 body
                    json                json


endpoint /api/v1/servidores -> Programa python -> json + codigo respuesta
                            ^
                            BBDD
    
    get
        Me tienen que dar algo JSON???
        Devuelvo: JSON con todos los servidores
    post
        Me tienen que dar algo? JSON con los datos del servidor
        Devuelvo... esos mismos datos... pero enriquecidos (ID)

endpoint /api/v1/servidores/{ID}
    get
    delete
    post

response_code:
    200 < OK
    300 < REDIRECCION
    400 < ERROR DEL CLIENTE
    500 < ERROR DEL SERVIDOR
    
JSON: Notación objetos JS

Objeto JS?
diccionario + metodos

3
"hola"
{ 
    'clave': 'valor'
}
[1,3]

YAML

YAML se ha comido a JSON... literalmente
{
'generico': {
    'clave1': 'valor1',
    'clave2': 'valor2'
    }
}
---
{ 
    'clave': 'valor'
}
---
'clave': 'valor'

#######################

/api/v1/servidores

Nombre
IP