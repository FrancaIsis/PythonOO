# Senac Minas Gerais/ Juiz de Fora
# Aluna: Isis França
# Turma: 0152
# Ano 2024
# Faça um programa que some a quantidade de números pares encontrados no intervalo entre 0 e 100.


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
    def mostrar_pares(self):
        pares=[]
        for i in self.lista:
            if i % 2 == 0:
                pares.append(i)
        return pares
    def soma_pares(self):
        soma = 0
        for i in self.lista:
            if i % 2 == 0:
                soma += i
        return soma


# entrada de dados
print('-'*70)
print('INTERVALO')
print('='*70)
comeco = int(input('Informe o primeiro número do intervalo desejado: '))
fim = int(input('Informe o último número do intervalo: '))
print('='*70)
minha_lista = Numero(comeco, fim)
soma = minha_lista.soma_pares()
print('-'*70)
print('O intervalo informado foi: ') 
print(minha_lista.mostrar_lista())
print(f'A soma dos numeros pares nesse intervalo é {soma}')
print('-'*70)