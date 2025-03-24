# test_calculadora.py
import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):

    def setUp(self):
        self.calc = Calculadora()

    def test_multiplicar(self):
        # Casos de prueba con números válidos
        self.assertEqual(self.calc.multiplicar(2, 3), 6)
        self.assertEqual(self.calc.multiplicar(-1, 5), -5)
        self.assertEqual(self.calc.multiplicar(0, 100), 0)

        # Casos de prueba con cadenas numéricas
        self.assertEqual(self.calc.multiplicar("2", "3"), 6)

        # Casos de prueba con entradas no numéricas
        self.assertEqual(self.calc.multiplicar("a", "b"), "Ingresa dos números válidos")  # Cambiado

if __name__ == "__main__":
    unittest.main()
