# Senac Minas Gerais/ Juiz de Fora
# Aluna: Isis França
# Turma: 0152
# Ano 2024
# Faça um programa que calcule os números primos em um intervalo pré-determinado pelo usuário.


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

    def mostrar_intervalo(self, inicio, fim):
        for i in range(self.inicio, self.fim + 1):
            print(i, end='|')

    def calcula_primo(self):
        for i in range(self.inicio, self.fim + 1):
            if i < 2:
                continue # ignora os primeiros numeros
            
            for j in range(2,i):
                if i%j == 0:
                    break
            else:
                print(i, end='|')
        


# entrada de dados

while True:
    inicio = input('Informe o primeiro número do intervalo: ')
    if inicio.isnumeric():
        fim = input('Informe o último número do intervalo: ')
        if fim.isnumeric():
            break
        else:
            print('Informe um numero válido.')
    else: 
        print('Informe um número válido.')

print('-'*70)
print('INTERVALO')

print('='*70)
minha_lista = Manipular_Intervalos(inicio, fim)

print('-'*70)
print('O intervalo informado foi: ') 
print(minha_lista.mostrar_intervalo(inicio, fim))
print('-'*70)

print(f'Os numeros primos no intervalo informado são:\n')
print(minha_lista.calcula_primo())