#  1. **Calculadora Simples** Implemente uma classe chamada `Calculadora` que tenha um método chamado `somar`. 
# Esse método deve ser sobrecarregado para aceitar dois ou três números e retornar a soma deles. 2.

import os


class Calculadora:
    # metodo construtor
    def __init__(self, n1, n2, n3=None):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
    # metodo que será sobrecarregado
    def somar(self):
        pass

# classe filha
class Operacoes_Calculadora(Calculadora):
    def __init__(self, n1, n2, n3=None):
        super().__init__(n1, n2, n3=None)
        
    def somar(self):
        if n3 is not None:
            soma = self.n1 + self.n2 + self.n3
            return soma
        else:
            soma = self.n1 + self.n2
            return soma


# classe para obter os numeros
class Numero:
    def __init__(self):
        pass
    def solictar_numeros(self, msg):
        while True:
            numero = input(msg)
            if numero.isnumeric() or numero is None:
                return int(numero)
                
            else:
                print('Informe um número válido: ')

# Declarações de variáveis:
minha_soma = object

# Limpeza do terminal:
os.system('cls' if os.name == 'nt' else 'clear')                

# entrada de dados:
print('-'*70)
print('CALCULADORA')
print('-'*70)


# instanciando os objetos
n = Numero()
print('Deseja somar dois ou três números?')
opcao = int(input('Digite 2 para somar dois numeros ou 3 para somar três números:'))
if opcao == 2:
    n1 = n.solictar_numeros('Informe o primeiro número: ')
    n2 = n.solictar_numeros('Informe o segundo número: ')
    
    minha_soma = Operacoes_Calculadora(n1, n2)
    soma = minha_soma.somar(n1,n2)
    print(f'O resultado da operação {n1} + {n2} é {soma}')
    
elif opcao == 3:
    n1 = n.solictar_numeros('Informe o primeiro número: ')
    n2 = n.solictar_numeros('Informe o segundo número: ')
    n3 = n.solictar_numeros('Informe o terceiro número: ')
    minha_soma = Operacoes_Calculadora(n1, n2, n3)
    soma = minha_soma.somar()
    print(f'O resultado da operação {n1} + {n2} + {n3} é {soma}')
else:
    print('Informe um valor válido:')






        

    
