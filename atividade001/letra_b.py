# Senac Minas Gerais/ Juiz de Fora
# Aluna: Isis França
# Turma: 0152
# Ano 2024
# Faça um programa que peça o ano do seu nascimento e calcule a sua idade 

import os
from datetime import datetime

class Idade:
    def __init__(self, nome, data_nasc):
        self.nome = nome
        self.data_nasc = data_nasc
    # Getters
    def get_nome(self):
        return self._nome
    def get_data_nasc(self):
        return self._data_nasc 
    
    # Setters
    def set_nome(self, value):
        self._nome = value
    def set_data_nasc(self, value):
        self._data_nasc = value 

    # metodos
    def calcula_idade(self):
        # calcula a data de hoje
        hoje = datetime.now()
        # converter a data de nascimento de string para obj datetime
        nascimento = datetime.strptime(self.data_nasc, '%d/%m/%Y')
        idade = hoje.year-nascimento.year -((hoje.month,hoje.day)<(nascimento.month, nascimento.day))
        return idade

# entrada de dados
print('-'*70)
print('CÁLCULO DA IDADE')
print('='*70)
nome = input('Digite seu nome: ')
data_nasc = input('Data de nascimento: (dd/mm/aaaa):')
print('-'*70)

# instanciando a classe
usuario = Idade(nome, data_nasc)

print('RESULTADO')
print('-'*70)
print(f'Nome: {usuario.nome}')
print(f'Data de nascimento: {usuario.data_nasc}')
print(f'Idade: {usuario.calcula_idade()} anos')


