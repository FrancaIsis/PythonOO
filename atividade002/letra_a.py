# Senac Minas Gerais/ Juiz de Fora
# Aluna: Isis França
# Turma: 0152
# Ano 2024
# Faça um programa que imprima os números no intervalo entre 1 e 100. Os números devem ser apresentados na horizontal


import os

class Numero:
    def __init__(self):
        self.lista = list(range(1,101))

    def get_numero(self):
        return self.lista
    #def set_numero(self, value):
    
    def mostrar_lista(self):
        for i in self.lista:
            print(i, end='|')

minha_lista = Numero()
print(minha_lista.mostrar_lista())