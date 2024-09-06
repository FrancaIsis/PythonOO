# Senac Minas Gerais/ Juiz de Fora
# Aluna: Isis França
# Turma: 0152
# Ano 2024
# Faça um programa com entrada de dados para calcular o perímetro de um retângulo. P=2(b+h)


import os

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def get_base(self):
        return self.base
    def get_altura(self):
        return self.altura
    def set_base(self, base):
        self.base = base
    def set_altura(self,altura):
        self.altura = altura
    
    def calcula_perimetro(self):
        perimetro = 2 * (self.base + self.altura)
        return perimetro

# entrada de dados
print('='*70)
base = int(input('Informe o valor da base do retângulo: '))
altura = int(input('Informe o valor da altura do retângulo: '))
print('='*70)

# instanciando a classe
retangulo = Retangulo(base, altura)
perimetro = retangulo.calcula_perimetro()

# saida de dados
print('='*70)
print(f'O perímetro do retângulo de base {base} e altura {altura} é: {perimetro}')
      
print('='*70)
