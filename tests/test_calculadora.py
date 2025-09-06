import unittest
from src.calculadora import Calculadora
from src.operacoes import adicionar, subtrair, multiplicar, dividir

class TestCalculadora(unittest.TestCase):

    def setUp(self):
        self.calculadora = Calculadora()

    def test_adicionar_operacao(self):
        self.calculadora.adicionar_operacao('14 - 8')
        self.assertEqual(len(self.calculadora.operacoes), 1)

    def test_processar_operacoes(self):
        self.calculadora.adicionar_operacao('14 - 8')
        self.calculadora.adicionar_operacao('5 * 6')
        resultados = self.calculadora.processar_operacoes()
        self.assertEqual(resultados, [6, 30])

    def test_calculo_penultima_operacao(self):
        self.calculadora.adicionar_operacao('2147483647 + 2')
        resultado = self.calculadora.processar_operacoes()
        self.assertEqual(resultado[-1], 2147483649)

    def test_divisao(self):
        self.calculadora.adicionar_operacao('18 / 3')
        resultado = self.calculadora.processar_operacoes()
        self.assertEqual(resultado[-1], 6)

    def test_imprimir_historico(self):
        self.calculadora.adicionar_operacao('14 - 8')
        self.calculadora.adicionar_operacao('5 * 6')
        self.calculadora.imprimir_historico()
        self.assertTrue(len(self.calculadora.operacoes) > 0)

if __name__ == '__main__':
    unittest.main()