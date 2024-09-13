# Senac Minas Gerais/ Juiz de Fora
# Aluna: Isis França
# Turma: 0152
# Ano 2024
# Faça um programa que imprima os números no intervalo entre 1 e 100. Os números devem ser apresentados na horizontal


import os

class Intervalo:
    # metodo construtor
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim

    def mostrar_intervalo(self, inicio, fim):
        pass # nao colocamos nada porque o metodo será sobrecarregado

# criando uma classe filha
class Mostrar(Intervalo): # passa como parametro a classe mãe
    # metodo construtor
    def __init__(self, inicio, fim):
        super().__init__(inicio, fim) # o proprio vscode ja preenche com a herança da classe super
    # metodo sobrecarregado
    def mostrar_intervalo(self):
        for i in range(self.inicio, self.fim):
            print(i, end='|')

# Declarações de variáveis:
minha_lacuna = object

# Limpeza do terminal:
os.system('cls' if os.name == 'nt' else 'clear')


# Instanciando o objeto
minha_lacuna = Mostrar(inicio=1, fim=101)

# mostrando resultados
print('-'*70)
print(f'Os numeros contidos no intervalo {minha_lacuna.inicio} e {minha_lacuna.fim -1} é:')
print('-'*70)

print(minha_lacuna.mostrar_intervalo())