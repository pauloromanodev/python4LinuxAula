#herança

class Pai():
    
    def __init__(self):
        self.nome = ''
        self.idade = 0
        self.nacionalidade = 'brasileira'
        
    def falar_portugues(self):
        print('Olá, como vai você?')
        

class Mae():

    def __init__(self):
        self.nome = ''
        self.idade = 0
        self.nacionalidade = 'argentina'
        
    def falar_ingles(self):
        print('Hello, how are you?')

    
        
class Filha(Pai, Mae):
    
    def __init__(self):
        Pai.__init__(self) #valores padrao (o ideal é nunca herdar classes que possuam mesmos atributos)
        self.profissao = ''
            
f1 = Filha()
print(f1.nacionalidade)
f1.nome = 'Gabriela'
f1.falar_portugues()
f1.falar_ingles()
