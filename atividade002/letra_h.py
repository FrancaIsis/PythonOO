# Senac Minas Gerais/ Juiz de Fora
# Aluna: Isis França
# Turma: 0152
# Ano 2024
# Faça um programa que imprima os valores no intervalo definidos pelo usuário.  
# Defina 3 números que deverão ser ignorados, ou seja, que não serão impressos na tela.


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
    def mostrar_lista_excecao(self,n1, n2, n3):
        for i in self.lista:
            if i == n1 or i == n2 or i == n3:
                continue
            print(i, end='|')



# entrada de dados
print('-'*70)
print('INTERVALO')
print('='*70)
comeco = int(input('Informe o primeiro número do intervalo desejado: '))
fim = int(input('Informe o último número do intervalo: '))
print('='*70)
minha_lista = Numero(comeco, fim)
soma = minha_lista.soma_pares()
primos = minha_lista.calcula_primo()
print('-'*70)
print('O intervalo informado foi: ') 
print(minha_lista.mostrar_lista())
print('-'*70)
primeiro_numero = int(input('Informe o primeiro numero a ser excluído: '))
segundo_numero = int(input('Informe o segundo numero a ser excluído: '))
terceiro_numero = int(input('Informe o terceiro numero a ser excluído: '))
print('-'*70)
print('A nova lista é:')
print('='*70)
print(minha_lista.mostrar_lista_excecao(primeiro_numero, segundo_numero, terceiro_numero))
print('-'*70)