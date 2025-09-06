import unittest
from src.operacoes import adicionar, subtrair, multiplicar, dividir

class TestOperacoes(unittest.TestCase):

    def test_adicionar(self):
        self.assertEqual(adicionar(2, 3), 5)
        self.assertEqual(adicionar(-1, 1), 0)
        self.assertEqual(adicionar(0, 0), 0)

    def test_subtrair(self):
        self.assertEqual(subtrair(5, 3), 2)
        self.assertEqual(subtrair(0, 1), -1)
        self.assertEqual(subtrair(-1, -1), 0)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(2, 3), 6)
        self.assertEqual(multiplicar(-1, 1), -1)
        self.assertEqual(multiplicar(0, 5), 0)

    def test_dividir(self):
        self.assertEqual(dividir(6, 3), 2)
        self.assertEqual(dividir(-6, 3), -2)
        with self.assertRaises(ZeroDivisionError):
            dividir(1, 0)

if __name__ == '__main__':
    unittest.main()