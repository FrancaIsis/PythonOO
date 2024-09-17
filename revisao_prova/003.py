import os


class Calculadora():
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
    
    def somar(self):
        soma = self.n1 + self.n2
        return soma

class Operacoes(Calculadora):
    def __init__(self, n1, n2):
        super().__init__(n1, n2)
    def somar(self):
        return super().somar()
    
calc = Operacoes(n1 = 2, n2 = 3)
soma = calc.somar()
print(soma)