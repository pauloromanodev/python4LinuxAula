from classes import *

c1 = Conta()
c1.conta = 123
c1.titular = 'Paulo'
c1.saldo = 0

c2 = Conta()
c2.conta = 456
c2.titular = 'Maria'
c2.saldo = 0

while True:

    print('1. Consultar Saldo')
    print('2. Realizar Saque')
    print('3. Efetuar Deposito')
    print('4. Fazer transferencia')
    print('5. Sair')
    print('----------------------')
    
    opc = input('Digite sua opção:')
    
    if opc == '1':
        c1.ver_saldo()        
        
    elif opc == '2':
        valor = float(input('Digite o valor para saque:'))
        c1.sacar(valor)
        
    elif opc == '3':
        valor = float(input('Digite o valor para deposito:'))
        c1.depositar(valor)        
        
    elif opc == '4':
        conta = int(input('Digite a conta de destino:'))
        
        if conta != c2.conta:
            print('Conta inexistente')
        else:            
            valor = float(input('Digite o valor para transferencia:'))
            c1.transferir(valor, c2)         
        
    elif opc == '5':
        break





