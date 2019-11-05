#criar uma classe de conta bancaria
#ela devera conter os seguintes atributos
# agencia
# conta
# titular
# saldo

#comportamentos:
# saque (validar se tem dinheiro), deposito, ver saldo


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
        
    def transferencia(self, valor, conta):
        if valor > self.saldo:
            return 'Saldo insuficiente.'
        else:
            self.saldo -= valor
            conta.saldo += valor

c = Conta()
c.conta = 123456
c.titular = 'Paulo Cesar'

c2 = Conta()
c2.conta = 999
c2.titular = 'Joaquim'

c.depositar(1500)
c.sacar(100)
c.ver_saldo()
c.sacar(1500)

c.transferencia(200, c2)

c.ver_saldo()
c2.ver_saldo()




