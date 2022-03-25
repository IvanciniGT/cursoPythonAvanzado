import requests

servicio="http://127.0.0.1:5000/api/v1/servidores"

def cuantos_objetos_hay():
    respuesta=requests.get(servicio)
    #print(respuesta.json())
    print(respuesta.status_code)
    return len(respuesta.json())


def nombre_primer_servidor():
    respuesta=requests.get(servicio)
    #print(respuesta.json())
    return respuesta.json()[0]['nombre']

def hacer_post():
    datos={
        'nombre': 'localhost' ,
        'descripcion': 'Entorno local' ,
        'ip': '127.0.0.1' ,
        'estado': True
    }
    respuesta=requests.post(servicio,json=datos)
    print(respuesta.json())
    print(respuesta.status_code)
    
#hacer_get()
#hacer_post()
#hacer_get()