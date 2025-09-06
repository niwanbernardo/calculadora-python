# File: /calculadora-python/src/main.py

from .calculadora import Calculadora

def main():
    calc = Calculadora()
    print("="*50)
    print("Bem-vindo à Calculadora Python!")
    print("="*50)
    print("Digite uma operação no formato: <número> <operador> <número>")
    print("Exemplo: 14 - 8")
    print("Operadores suportados: +  -  *  /")
    print("Digite 'sair' para encerrar.\n")
    
    while True:
        print("-"*50)
        user_input = input("Digite uma operação: ")
        
        if user_input.lower() == 'sair':
            print("\nEncerrando calculadora. Até logo!")
            print("="*50)
            break
        
        try:
            partes = user_input.split()
            if len(partes) != 3:
                raise ValueError("Formato inválido. Use: <número> <operador> <número>")
            if partes[1] not in ['+', '-', '*', '/']:
                raise ValueError("Operador inválido. Use apenas: +  -  *  /")
            # Tenta converter os números
            float(partes[0])
            float(partes[2])
            
            calc.adicionar_operacao(user_input)
            print("\n✅ Operação adicionada com sucesso!")
            calc.processar_operacoes()
            calc.imprimir_historico()
            calc.imprimir_pilha()
        except Exception as e:
            print(f"\nErro: {e}\nPor favor, tente novamente.\n")

if __name__ == "__main__":
    main()