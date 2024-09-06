# Senac Minas Gerais/ Juiz de Fora
# Aluna: Isis França
# Turma: 0152
# Ano 2024
# Faça um programa que receba e divida 2 números. A saída da divisão precisará ser formatada com 4 casas decimais.


import os

class Divisao:
    def __init__(self, dividendo, divisor):
        self.set_dividendo(dividendo)
        self.set_divisor(divisor)

    # Getters
    def get_dividendo(self):
        return self._dividendo
    def get_divisor(self):
        return self._divisor
    
    # Setters
    def set_dividendo(self, value):
        self._dividendo = value
    def set_divisor(self, value):
        if value == 0:
            raise ValueError('O divisor não poder ser igual a zero')
        else:
            self._divisor = value
    
    def dividir(self):
        resultado = self._dividendo/self._divisor
        return '{:.4f}'.format(resultado)# retorna com 4 casas decimais

# entrada de dados
print('='*70)
dividendo = float(input('Informe o valor do dividendo: '))
divisor = float(input('Informe o valor do divisor: '))
print('='*70)
# instanciando a classe
try:
    d = Divisao(dividendo,divisor)
    # exibindo resultado
    print('-'*70)
    print(f'O resuldado da divisão de {dividendo} por {divisor} é {d.dividir()}')
    print('-'*70)
except ValueError as e:
    print(e)
    print('-'*70)