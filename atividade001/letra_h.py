# Senac Minas Gerais/ Juiz de Fora
# Aluna: Isis França
# Turma: 0152
# Ano 2024
# Faça um programa que receba um número inteiro, depois imprima sua tabuada de multiplicação.


import os


class Numeral:
    def __init__(self, numero):
        self.numero = numero
    # Getters
    def get_numero(self):
        return self.numero
    # Setters
    def set_numero(self, value):
        self.numero = value
    # Método
    def calcula_tabuada(self):
        for i in range (0,10):
            resultado = i * self.numero
            print(f'{self.numero} X {i} = {resultado}')

# entrada de dados
print('-'*70)
print('TABUADA')
print('='*70)
numero = int(input('Informe um número: '))
print('='*70)

# instanciando a classe
n = Numeral(numero)
tabuada = n.calcula_tabuada()

# saida de dados
print('='*70)
print(tabuada)