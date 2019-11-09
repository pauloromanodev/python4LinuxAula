import time

vermelho = int(input('Digite o tempo do farol vermelho:'))
verde = int(input('Digite o tempo do farol verde:'))
amarelo = int(input('Digite o tempo do farol amarelo:'))

while True:
    
    print('Farol Vermelho')    
    time.sleep(vermelho)

    print('Farol Verde')    
    time.sleep(verde)
    
    print('Farol Amarelo')    
    time.sleep(amarelo)
