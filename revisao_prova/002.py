# Faça um programa que peça 3 valores , 
# depois calcule e imprima  a soma e a multiplicação desses valores. 

import os

class Calculadora():
    # método construtor
    def __init__(self, n1, n2, n3):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
    # método para somar
    def somar(self):
        soma = self.n1 + self.n2 + self.n3
        return soma
    # método para multiplicar
    def multiplicar(self):
        multi = self.n1 * self.n2 * self.n3
        return multi
    
# classe para obter os numeros
class Numero():
    # método construtor
    def __init__(self):
        pass
    def solicita_numero(self, msg):
        while True:
            numero = input(msg)
            if numero.isnumeric():
                return int(numero)
            else:
                print('Informe um numero válido.')

# declarando variáveis
calc = object
n = object

# Limpeza do terminal:
os.system('cls' if os.name == 'nt' else 'clear')  

print('-'*70)
print('CALCULADORA')
print('-'*70)

# instanciando objeto
n = Numero()

# entrada de dados
n1 = n.solicita_numero('Informe o primeiro número:')
n2 = n.solicita_numero('Informe o segundo número:')
n3 = n.solicita_numero('Informe o terceiro número:')

# instanciando objeto
calc = Calculadora(n1,n2,n3)

soma = calc.somar()
multi = calc.multiplicar()

# saída de dados
print(f'O resultado da soma de {n1} + {n2} + {n3} é {soma}')
print(f'O resultado da multiplicação entre {n1} x {n2} x {n3} é {multi}')

    