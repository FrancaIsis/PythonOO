# Senac Minas Gerais/ Juiz de Fora
# Aluna: Isis França
# Turma: 0152
# Ano 2024
# Faça um programa que peça 3 valores , depois calcule e imprima  a soma e a multiplicação desses valores. 

import os


class Calculadora:
    def __init__(self,a,b,c): #metodo construtor
        #chamar o setter para definir os valores de a,b e c
        self.set_a(a)
        self.set_b(b)
        self.set_c(c)

    #getters
    def get_a(self):
        return self._a
    def get_b(self):
        return self._b
    def get_c(self):
        return self._c 

    #setters
    def set_a(self, value):
        self._a = value
    def set_b(self,value):
        self._b = value
    def set_c(self,value):
        self._c = value


    def somar(self):
        soma = self._a + self._b + self._c
        return soma
    
    def multiplicar(self):
        multiplica = self._a * self._b * self._c
        return multiplica
    
    def subtrair(self):
        subtrai = self._a - self._b - self._c
        return subtrai
    
    def dividir(self):
        divide = self._a / self._b / self._c
        return divide

escolha = 0
while escolha != 5:
    os.system('cls')

    print('-'*70)
    print('CALCULADORA')
    print('-'*70)

    # entrada de dados
    a = int(input('Digite o primeiro numero:'))
    b = int(input('Digite o segundo numero:'))
    c = int(input('Digite o terceiro numero:'))
    print('-'*70)

    # processamento
    operacao = Calculadora(a,b,c)
    soma = operacao.somar()
    multiplicacao = operacao.multiplicar()
    subtracao = operacao.subtrair()
    divisao = operacao.dividir()

    # saída
    print(f'Os numeros escolhidos foram {a}, {b}, {c}:')
    print('Qual operação deseja realizar?')
    escolha = int(input('1 - soma\n2 - subtração\n3 - multiplicação\n4 - Divisão\n5 - Sair\n'))
    if escolha == 1:
        print(f'A soma de {a} + {b} + {c} é {soma}')
    elif escolha == 2:
        print(f'A subtração de {a} - {b} - {c} é {subtracao}')
    elif escolha == 3:
        print(f'A multiplicação de {a} x {b} x {c} é {multiplicacao}')
    elif escolha == 4:
        print(f'A divisão de {a} / {b} / {c} é {divisao}')
    else:
        print('Encerrando...')
        break
    input('\nPressione Enter para continuar...')