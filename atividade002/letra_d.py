# Senac Minas Gerais/ Juiz de Fora
# Aluna: Isis França
# Turma: 0152
# Ano 2024
# Faça um programa que imprima os números pares entre 0 e 100.


import os
# classe mãe
class Intervalo:
    # metodo construtor
    def __init__(self, inicio, fim):
        self.inicio = int(inicio)
        self.fim = int(fim)

    def mostrar_intervalo(self, inicio, fim):
        pass # nao colocamos nada porque o metodo será sobrecarregado

# # classe filha
# class Mostrar(Intervalo): # passa como parametro a classe mãe
#     # metodo construtor
#     def __init__(self, inicio, fim):
#         super().__init__(inicio, fim) # o proprio vscode ja preenche com a herança da classe super
#     # metodo sobrecarregado
#     def mostrar_intervalo(self):
#         for i in range(self.inicio, self.fim + 1):
#             print(i, end='|')

# # classe filha
# class Mostrar_Invertido(Intervalo):
#     def __init__(self, inicio, fim):
#         super().__init__(inicio, fim)
#     def mostrar_intervalo(self, inicio, fim):
#         for i in reversed (range(self.inicio, self.fim + 1)):
#             print(i, end='|')

class Mostrar_Pares(Intervalo):
    def __init__(self, inicio, fim):
        super().__init__(inicio, fim)
    def mostrar_intervalo(self, inicio, fim):
        for i in range(self.inicio, self.fim + 1):
            if i % 2 == 0:
                print(i, end='|')


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
print(minha_lista.mostrar_intervalo(inicio, fim))