import unittest
#. Mock
import requests_mock

from cliente import cuantos_objetos_hay, nombre_primer_servidor

class TestCliente(unittest.TestCase):
    
    def setUp(self):
        self.mi_moco=requests_mock.Mocker()
        self.mi_moco.register_uri('GET','/api/v1/servidores',
            json=[{
                'nombre': 'localhost',
                'descripcion': 'Entorno Local',
                'estado': True,
                'ip': '127.0.0.1'
            },
            {
                'nombre': 'servidor.produccion',
                'descripcion': 'Entorno produccion',
                'estado': True,
                'ip': '171.100.100.100'
            }], status_code=201
        )
    
    def test_cuantos_objetos_hay(self):
        with self.mi_moco:
            resultado=cuantos_objetos_hay()
            self.assertTrue(resultado==2)

    def test_nombre_primer_servidor(self):
        with self.mi_moco:
            resultado=nombre_primer_servidor()
            self.assertTrue(resultado=='localhost')


if __name__ == '__main__':
    unittest.main()
