import unittest
from 4-pruebas-unitarias import Test_LibreriaOperacionesMatematicas()
suite=unittest.TestSuite()
suite.addTest(Test_LibreriaOperacionesMatematicas)

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite) 
