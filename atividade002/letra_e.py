# Senac Minas Gerais/ Juiz de Fora
# Aluna: Isis França
# Turma: 0152
# Ano 2024
# Faça um programa que some a quantidade de números pares encontrados no intervalo entre 0 e 100.


import os
# classe mãe
class Intervalo:
    # metodo construtor
    def __init__(self, inicio, fim):
        self.inicio = int(inicio)
        self.fim = int(fim)

    def mostrar_intervalo(self, inicio, fim):
        pass # nao colocamos nada porque o metodo será sobrecarregado

class Mostrar_Pares(Intervalo):
    def __init__(self, inicio, fim):
        super().__init__(inicio, fim)
    def mostrar_intervalo(self, inicio, fim):
        soma = 0
        for i in range(self.inicio, self.fim + 1):
            if i % 2 == 0:
                soma += i
        return soma

            
# Declarações de variáveis:
minha_lista = object

# Limpeza do terminal:
os.system('cls' if os.name == 'nt' else 'clear')

# entrada de dados
print('-'*70)
print('INTERVALO')
print('='*70)
inicio = 0
fim = 100
print('='*70)
minha_lista = Mostrar_Pares(inicio, fim)
soma_pares = minha_lista.mostrar_intervalo(inicio, fim)
print(f'A soma dos numeros pares nesse intervalo é {soma_pares}')



