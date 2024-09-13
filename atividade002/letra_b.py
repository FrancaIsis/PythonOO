# Senac Minas Gerais/ Juiz de Fora
# Aluna: Isis França
# Turma: 0152
# Ano 2024
# Evolua o programa anterior para um código que pergunte ao usuário qual o intervalo que ele deseja ver impresso.


import os

# classe mãe
class Intervalo:
    # metodo construtor
    def __init__(self, inicio, fim):
        self.inicio = int(inicio)
        self.fim = int(fim)

    def mostrar_intervalo(self, inicio, fim):
        pass # nao colocamos nada porque o metodo será sobrecarregado

# classe filha
class Mostrar(Intervalo): # passa como parametro a classe mãe
    # metodo construtor
    def __init__(self, inicio, fim):
        super().__init__(inicio, fim) # o proprio vscode ja preenche com a herança da classe super
    # metodo sobrecarregado
    def mostrar_intervalo(self):
        for i in range(self.inicio, self.fim + 1):
            print(i, end='|')

# solicitando dados do usuario
while True:
    inicio = input('Digite o primeiro numero do intervalo: ')
    if inicio.isnumeric():
        fim = input('Digite o segundo numero do intervalo: ')
        if fim.isnumeric():
            break
        else:
            print('Valor inválido.')
    else:
        print('Valor inválido.')


# Declarações de variáveis:
minha_lacuna = object

# Limpeza do terminal:
os.system('cls' if os.name == 'nt' else 'clear')

# Instanciando o objeto
minha_lacuna = Mostrar(inicio, fim)

# mostrando resultados
print('-'*70)
print(f'Os numeros contidos no intervalo {minha_lacuna.inicio} e {minha_lacuna.fim} é:')
print('-'*70)

print(minha_lacuna.mostrar_intervalo())

