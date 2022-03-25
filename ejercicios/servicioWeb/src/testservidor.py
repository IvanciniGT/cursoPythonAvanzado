from servicio import montarServidorFlask

import unittest

class TestCliente(unittest.TestCase):
    
    def setUp(self):
        self.servidor_flask=montarServidorFlask("configuracion.test")
        self.servidor_flask.config['TESTING']=True
        self.cliente=self.servidor_flask.test_client()
    
    def test_get(self):
        respuesta=self.cliente.get("/api/v1/servidores")
        print(respuesta.json)
        self.assertEqual(respuesta.status_code,200)

#    def test_post(self):
#        pass


if __name__ == '__main__':
    unittest.main()


"""
import time
import requests
from threading import Thread
    def setUp(self):
        self.servidor_flask=montarServidorFlask("configuracion.test")
        Thread(target= lambda: self.servidor_flask.run()).start()

    def test_get(self):
        time.sleep(2)
        respuesta=requests.get("http://localhost:5000/api/v1/servidores")
        print(respuesta.json)
        self.assertEqual(respuesta.status_code,201)
"""