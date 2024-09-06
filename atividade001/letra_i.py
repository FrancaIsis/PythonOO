# Senac Minas Gerais/ Juiz de Fora
# Aluna: Isis França
# Turma: 0152
# Ano 2024
# Faça um programa que receba um valor em reais, depois calcule quantos dólares daria para comprar com esse valor.


import os

class Casa_da_Moeda:
    def __init__(self, valor,preco_moeda):
        self.valor = valor
        self.preco_moeda = preco_moeda
    
    # Getters
    def get_valor(self):
        return self.valor
    def get_preco_moeda(self):
        return self.preco_moeda

    # Setters
    def set_valor(self, value):
        self.valor = value
    def set_preco_moeda(self, preco):
        self.preco_moeda = preco

    # Metodo
    def converte_real_dolar(self):
        quantidade_dolar = self.valor/ self.preco_moeda
        return quantidade_dolar

# entrada de dados
print('='*70)
valor = float(input('Quantos reais você tem? '))
preco_moeda = float(input('Qual o preço do dolar? '))
print('='*70)

# instanciando a classe
rico = Casa_da_Moeda(valor,preco_moeda)
quantidade_dolar = rico.converte_real_dolar()

# saida de dados
print('='*70)
print(f'Você tem {valor} reais.\nCom esse dinheiro você consegue comprar {quantidade_dolar:.2f} dolares')
      
print('='*70)