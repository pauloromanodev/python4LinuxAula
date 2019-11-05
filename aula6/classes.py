
class Conta():
    
    def __init__(self):
        self.agencia = '1'
        self.conta = 0
        self.titular = ''
        self.saldo = 0
        
    def sacar(self, valor):
        if valor < self.saldo:
            self.saldo -= valor
            print('Saque realizado com sucesso!')
        else:
            print('Saldo insuficiente')
        
    def depositar(self, valor):
        self.saldo += valor
        print('Deposito realizado com sucesso!')
        
    def ver_saldo(self):
        print('O seu saldo é:', self.saldo)
        
    def transferir(self, valor, conta):
        if valor > self.saldo:
            return 'Saldo insuficiente.'
        else:
            self.saldo -= valor
            conta.saldo += valor
            
