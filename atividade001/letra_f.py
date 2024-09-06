# Senac Minas Gerais/ Juiz de Fora
# Aluna: Isis França
# Turma: 0152
# Ano 2024
# Faça um programa que receba um número qualquer e calcule o dobro e o triplo desse número.


import os

class Numeros:
    def __init__(self, numero):
        self.set_numero(numero)
    
    # Getters
    def get_numero(self):
        return self._numero
    
    # Setters
    def set_numero(self, value):
        self._numero = value

    # metodo
    def calcula_dobro_triplo(self):
        dobro = self._numero * 2
        triplo = self._numero * 3
        return dobro, triplo
    
# entrada de dados
print('='*70)
numero = int(input('Informe um número: '))
print('='*70)

# instanciando a classe
n = Numeros(numero)
dobro, triplo = n.calcula_dobro_triplo()

# saida de dados
print('='*70)
print(f'O número informado foi {numero}.\nSeu dobro é {dobro}'
      f'\nSeu triplo é {triplo}')
print('='*70)