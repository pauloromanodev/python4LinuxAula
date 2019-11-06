import unittest
from ex01 import *

c = Carro('Fusca', 'Vermelho', 0)

class testeFuncoes(unittest.TestCase):
    
    def test_funcAcelerar(self):
        self.assertEqual(50,c.acelerar(50))
        
    def test_funcFrear(self):
        self.assertEqual(0,c.frear(50))
            
    def test_funcCor(self):
        self.assertEqual('Vermelho',c.getCor())
        
    def test_funcModelo(self):
        self.assertEqual('Fusca',c.getModelo())

if __name__ == '__main__':
    unittest.main()
