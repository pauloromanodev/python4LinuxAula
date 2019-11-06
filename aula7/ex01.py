class Carro:
    
    def __init__(self, modelo, cor, velocidade):
        self.modelo = modelo
        self.cor = cor
        self.velocidade = velocidade
        
    def getModelo(self):
        return self.modelo
        
    def setModelo(self, valor):
        self.modelo = valor
        
    def getCor(self):
        return self.cor
        
    def setCor(self, valor):
        self.cor = valor
        
    def getVelocidade(self):
        return self.velocidade
        
    def setVelocidade(self, valor):
        self.velocidade = valor
        
    def acelerar(self, valor):
        self.velocidade += valor
        return self.velocidade
        
    def frear(self, valor):
        self.velocidade -= valor
        return self.velocidade
        
c = Carro('Fusca', 'Vermelho', 0)
c.acelerar(50)
c.getVelocidade()
c.frear(50)
c.getVelocidade()

        
