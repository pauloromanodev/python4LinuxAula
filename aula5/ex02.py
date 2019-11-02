#classes

class Carro():
    
    #construtor
    def __init__(self, modelo = '', cor = '', velocidade = 0, ano = 0):
        self.modelo = modelo
        self.cor = cor
        self.velocidade = velocidade
        self.ano = ano
        
    def acelerar(self):
        self.velocidade += 10
        
    def frear(self):
        if self.velocidade == 0:
            print('O carro está parado')
        else:
            self.velocidade -= 10
        
fusca = Carro('Fusca', 'Vermelho', 0, 1975)
verona = Carro()

print(fusca.modelo)
print(fusca.cor)
print(fusca.velocidade)

fusca.acelerar()
fusca.acelerar()

print(fusca.velocidade)
