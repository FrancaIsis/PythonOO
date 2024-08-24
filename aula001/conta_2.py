import os


class Banco():
    def __init__(self, nome='', agencia=0, conta=0, cpf=0,
                 conta_corrente=0, poupanca=0):
        self.nome = nome
        self.agencia = agencia
        self.conta = conta
        self.cpf = cpf
        self.conta_corrente = conta_corrente
        self.poupanca = poupanca

    def deposito(self, valor):
        escolha = input(
            'Conta Corrente (cc) ou Poupança (po)? ').lower().strip()

        if escolha == 'cc':
            print(f'Valor do depósito: (+)R${valor}')
            print(f'Saldo anterior (CC): R${self.conta_corrente}')
            self.conta_corrente += valor
            print(f'\tSaldo atual na Conta Corrente: R${self.conta_corrente}')
            print('-'*70)

        elif escolha == 'po':
            print(f'\nValor do deposito: (+)R${valor}')
            print(f'\Saldo anterior na Poupança: R${self.poupanca}')
            self.poupanca += valor
            print(f'\tSaldo atual na Poupança: R$ {self.poupanca}')
            print('-'*70)
            
        else:
            print('Opção inválida!')
            
    def saque(self, valor):
        escolha = input('Conta corrente (cc) ou Poupança (po)?').lower().strip()
        
        if escolha == 'cc':
            print(f'\nValor sacado: (- )R${valor}')
            print(f'\Saldo anterior em Poupança: R${self.poupanca}')
            self.poupanca -= valor
            print(f'\tSaldo atual na poupança: R${self.poupanca}')
            print('-'*70)
        else:
            print('Opção inválida!')
            
os.system('cls')

# Coletar dados do usuário para criar uma nova conta
        