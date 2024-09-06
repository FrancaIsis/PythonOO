# Senac Minas Gerais/ Juiz de Fora
# Aluna: Isis França
# Turma: 0152
# Ano 2024
# Faça um programa que receba um número inteiro e mostre o sucessor e antecessor.


import os

class Numero:
    def __init__(self, numero):
        self.set_numero(numero)
    
    # Getters
    def get_numero(self):
        return self._numero
    
    # Setters
    def set_numero(self, value):
        self._numero = value

    # metodo
    def calcula_antecessor_sucessor(self):
        antecessor = self._numero - 1
        sucessor = self._numero + 1
        return antecessor, sucessor
    
# entrada de dados
print('='*70)
numero = int(input('Informe um número: '))
print('='*70)

# instanciando a classe
n = Numero(numero)
antecessor, sucessor = n.calcula_antecessor_sucessor()

# saida de dados
print('='*70)
print(f'O número informado foi {numero}.\nSeu antecessor é {antecessor}'
      f'\nSeu sucessor é {sucessor}')
print('='*70)