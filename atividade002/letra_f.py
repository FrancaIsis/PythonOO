# Senac Minas Gerais/ Juiz de Fora
# Aluna: Isis França
# Turma: 0152
# Ano 2024
# Faça um programa que imprima os números primos entre 0 e 100.
# Um número natural é primo se for maior que 1 e for divisível apenas por 1 e por ele mesmo


import os


class Numero:
    def __init__(self, comeco, fim):
        self.comeco = 0
        self.fim = 100
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
    def calcula_primo(self):
        primos = []
        for i in self.lista:
            if i < 2:
                continue # ignora os primeiros numeros
            somatorio = 0
            for j in range(1,1+i):
                if i%j == 0:
                    somatorio += 1
            if somatorio == 2:
                primos.append(i)
        return primos


# entrada de dados
print('-'*70)
print('INTERVALO')
print('='*70)
#comeco = int(input('Informe o primeiro número do intervalo desejado: '))
#fim = int(input('Informe o último número do intervalo: '))
print('='*70)
minha_lista = Numero(comeco=0, fim=100)
soma = minha_lista.soma_pares()
primos = minha_lista.calcula_primo()
print('-'*70)
print('O intervalo informado foi: ') 
print(minha_lista.mostrar_lista())
print('-'*70)

print(f'Os numeros primos no intervalo informado são:\n{primos}')
