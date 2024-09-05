# Senac Minas Gerais/ Juiz de Fora
# Aluna: Isis França
# Turma: 0152
# Ano 2024
# Faça um programa que peça 4 notas, após a entrada de dados calcular a média das notas digitadas.


import os

class Media:
    # metodo construtor
    def __init__(self):
        self.notas = []

    # Getters

    # Setters

    def calcula_media(self, soma):
        media = soma/len(self.notas)
        return media

    def solicita_notas(self):
        notas = []
        soma = 0
        for n in range(1,5):
            self.notas.append(float(input(f'Digite a {n}° nota: ')))
        soma = sum(self.notas)
        return soma, self.notas


# instanciando a classe
media1 = Media()

# entrada de dados
soma_notas, valor_notas = media1.solicita_notas()

# processamento
media_aluno = media1.calcula_media(soma_notas)

# saida de dados
print('RESULTADO')
print('-'*70)
print(f'As notas informadas foram:')
for n, nota in enumerate (valor_notas):
    print(f'{n+1}° nota: {nota}')

print(f'O valor da media é {media_aluno:.2f}')


