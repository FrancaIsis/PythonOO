# Senac Minas Gerais/ Juiz de Fora
# Aluna: Isis França
# Turma: 0152
# Ano 2024
# Faça um programa que imprima os números no intervalo entre 1 e 10 em ordem inversa.


import os
class Numero:
    def __init__(self, comeco, fim):
        self.comeco = comeco
        self.fim = fim
        self.lista = list(range(comeco,fim+1))

    def get_comeco(self):
        return self.comeco
    def get_fim(self):
        return self.fim
    def get_lista(self):
        return self.lista
    
    def set_comeco(self, value):
        self.comeco = value
    def set_fim(self, value):
        self.fim = value
    
    
    def mostrar_lista(self):
        for i in self.lista:
            print(i, end='|')
    def mostrar_lista_inversa(self):
        for i in reversed (self.lista):
            print(i, end='|')

# entrada de dados
print('-'*70)
print('INTERVALO')
print('='*70)
comeco = int(input('Informe o primeiro número do intervalo desejado: '))
fim = int(input('Informe o último número do intervalo: '))
print('='*70)
minha_lista = Numero(comeco, fim)
print(minha_lista.mostrar_lista_inversa())