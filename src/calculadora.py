from .stack import Stack
from .operacoes import adicionar, subtrair, multiplicar, dividir

class Operacao:
    def __init__(self, expressao):
        self.expressao = expressao
        self.valorA = None
        self.valorB = None
        self.operador = None
        self.resultado = None
        self.parse_expressao()

    def parse_expressao(self):
        partes = self.expressao.split()
        if len(partes) == 3:
            try:
                self.valorA = float(partes[0])
                self.operador = partes[1]
                self.valorB = float(partes[2])
            except ValueError:
                raise ValueError("Os valores devem ser números válidos.")

    def calcular(self):
        if self.operador == '+':
            self.resultado = adicionar(self.valorA, self.valorB)
        elif self.operador == '-':
            self.resultado = subtrair(self.valorA, self.valorB)
        elif self.operador == '*':
            self.resultado = multiplicar(self.valorA, self.valorB)
        elif self.operador == '/':
            self.resultado = dividir(self.valorA, self.valorB)
        else:
            raise ValueError("Operador inválido")
        return self.resultado

    def __str__(self):
        return f"{self.valorA} {self.operador} {self.valorB}"

class Calculadora:
    def __init__(self):
        self.operacoes = []
        self.pilha_resultados = Stack()
    
    def adicionar_operacao(self, expressao):
        operacao = Operacao(expressao)
        self.operacoes.append(operacao)
    
    def processar_operacoes(self):
        print("\n" + "="*40)
        print("🔢 Resultados das Operações")
        print("="*40)
        resultados = []
        for operacao in self.operacoes:
            if operacao.resultado is None:  # Só processa se ainda não foi processada
                try:
                    resultado = operacao.calcular()
                    self.pilha_resultados.push(resultado)
                    resultados.append(resultado)
                    print(f"→ {operacao} = {resultado}")
                except Exception as e:
                    operacao.resultado = f"Erro: {e}"  # Marca como processada com erro
                    print(f"→ {operacao} = Erro: {e}")
        print("="*40 + "\n")
        return resultados
    
    def imprimir_historico(self):
        print("\n📜 Histórico de Operações:")
        for idx, operacao in enumerate(self.operacoes, 1):
            print(f"{idx}. {operacao}")
        print()
    
    def imprimir_pilha(self):
        print("📦 Pilha de Resultados:")
        self.pilha_resultados.print_stack()
        print()