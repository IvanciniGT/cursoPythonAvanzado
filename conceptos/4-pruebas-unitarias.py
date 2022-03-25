import unittest

class LibreriaOperacionesMatematicas:
    
    @staticmethod
    def suma(numero1, numero2):
        return numero1+numero2

    @staticmethod
    def resta(numero1, numero2):
        return numero1-numero2

    @staticmethod
    def division(numero1, numero2):
        return numero1/numero2


class Test_LibreriaOperacionesMatematicas(unittest.TestCase):
    
    def test_SumarNumerosPositivos(self):
        resultado=LibreriaOperacionesMatematicas.suma(5,8)
        self.assertTrue(resultado==13)
    
    def test_SumarNumerosNegativos(self):
        resultado=LibreriaOperacionesMatematicas.suma(5,-8)
        self.assertEqual(resultado,-3)
    
    def test_SumarCero(self):
        resultado=LibreriaOperacionesMatematicas.suma(5,0)
        self.assertTrue(resultado==5)

    def test_RestarNumerosPositivos(self):
        resultado=LibreriaOperacionesMatematicas.resta(5,8)
        self.assertTrue(resultado==-3)
    
    def test_RestarNumerosNegativos(self):
        resultado=LibreriaOperacionesMatematicas.resta(5,-8)
        self.assertTrue(resultado==13)
    
    def test_RestarCero(self):
        resultado=LibreriaOperacionesMatematicas.resta(5,0)
        #MUCHO CODIGO
        self.assertTrue(resultado==5)
        
    def test_DivisionEntreCero(self):
        self.assertRaises(ZeroDivisionError, 
            lambda: LibreriaOperacionesMatematicas.division(5,0)
        )
        """
        try:
            ejecutarLaFuncionQueMeSuministren
        except:
            return
        raise AssertionError("No funciona la division entre 0.. No ha generado error")
        """
"""
probador=Test_LibreriaOperacionesMatematicas()
probador.test_SumarNumerosPositivos()
probador.test_SumarNumerosNegativos()
probador.test_SumarCero()
probador.test_RestarNumerosPositivos()
probador.test_RestarNumerosNegativos()
probador.test_RestarCero()
"""
if __name__ == '__main__':
    unittest.main()

# Prueba 3 formas:
#.  OK
#.  FALLO   No se cumple el assert
#.  ERROR.  Explotó

