# Senac Minas Gerais/ Juiz de Fora
# Aluna: Isis França
# Turma: 0152
# Ano 2024
# Faça um programa que imprima os valores no intervalo definidos pelo usuário.  
# Defina 3 números que deverão ser ignorados, ou seja, que não serão impressos na tela.


import os
# classe mãe
class Intervalo:
    # metodo construtor
    def __init__(self, inicio, fim):
        self.inicio = int(inicio)
        self.fim = int(fim)

    def mostrar_intervalo(self, inicio, fim):
        pass # nao colocamos nada porque o metodo será sobrecarregado
   
class Manipular_Intervalos(Intervalo):
    def __init__(self, inicio, fim):
        super().__init__(inicio, fim)

    def mostrar_intervalo(self):
        for i in range(self.inicio, self.fim + 1):
            print(i, end='|')

    def mostrar_intervalo_excecao(self,n1, n2, n3):
        n1 = int(n1)
        n2 = int(n2)
        n3 = int(n3)
        for i in range(self.inicio, self.fim+1):
            if i == n1 or i == n2 or i == n3:
                continue
            print(i, end='|')

class Numero:
    def __init__(self):
        #self.numero = numero
        pass
    def obter_numero(self,msg):
        while True:
            numero = input(msg)
            if numero.isnumeric:
                return int(numero)
            else:
                print('Informe um número inteiro válido: ')
        


# entrada de dados

print('-'*70)
print('INTERVALO')
print('='*70)

n = Numero()
inicio = n.obter_numero('Infome o primeiro número do intervalo: ')
fim = n.obter_numero('Infome o último número do intervalo: ')
n1 = n.obter_numero('Infome o primeiro número a ser ignorado: ')
n2 = n.obter_numero('Infome o segundo número a ser ignorado: ')
n3 = n.obter_numero('Infome o terceiro número a ser ignorado: ')

minha_lista = Manipular_Intervalos(inicio, fim)

print('-'*70)
print('O intervalo escolhido foi: ') 
print(minha_lista.mostrar_intervalo_excecao(n1, n2, n3))
print('-'*70)

print(f'Os numeros excluídos foram {n1}, {n2}, {n3}')
