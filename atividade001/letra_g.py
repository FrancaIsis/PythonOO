# Senac Minas Gerais/ Juiz de Fora
# Aluna: Isis França
# Turma: 0152
# Ano 2024
# Faça um programa que converta metros em centímetros e milímetros.


import os

class Conversao:
    def __init__(self, medida):
        self.set_medida(medida)
    
    # Getters
    def get_medida(self):
        return self._medida

    # Setters
    def set_medida(self, value):
        self._medida = value

    # Metodo
    def converte_metro_centrimeto(self):
        medida_centimetro = self._medida * 100
        return medida_centimetro
    def converte_metro_milimetro(self):
        medida_milimetro = self._medida * 1000
        return medida_milimetro
    
# entrada de dados
print('='*70)
medida = int(input('Informe a medida em metros: '))
print('='*70)

# instanciando a classe
c = Conversao(medida)
medida_centimetro = c.converte_metro_centrimeto()
medida_milimetro = c.converte_metro_milimetro()

# saida de dados
print('='*70)
print(f'A medida informada foi {medida} mt.\nSeu equivalente em centímetros é {medida_centimetro} cm'
      f'\nSeu equivalente em milímetros é {medida_milimetro} mm')
print('='*70)