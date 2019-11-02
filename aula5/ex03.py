#classes

class Onibus():
    
    #construtor
    def __init__(self, capacidade = 0, ocupacao = 0, velocidade = 0, origem = '', destino = ''):
        self.capacidade = capacidade
        self.ocupacao = ocupacao
        self.velocidade = velocidade
        self.origem = origem
        self.destino = destino
        
    def acelerar(self):
        self.velocidade += 20
        
    def frear(self):
        if self.velocidade == 0:
            print('O ônibus está parado')
        else:
            self.velocidade -= 20
            
    def embarcar(self, quantidade):        
        
        if (self.ocupacao + quantidade) > self.capacidade:
            print('O ônibus está cheio')
        else:
            self.ocupacao += quantidade
    

bus = Onibus(50, 0, 0, 'SP', 'MG')
        
while True:
    
    print('1. Embarcar pessoa')
    print('2. Acelerar')
    print('3. Frear')
    print('4. Sair')
    print('------------------')
    
    opc = input('Digite sua opção:')
    
    if opc == '1':
        pessoas = int(input('Digite quantas pessoas:'))
        bus.embarcar(pessoas)
        print(bus.ocupacao)
        
    elif opc == '2':
        bus.acelerar()
        print(bus.velocidade)
        
    elif opc == '3':
        bus.frear()    
        print(bus.velocidade)
        
    elif opc == '4':
        break
