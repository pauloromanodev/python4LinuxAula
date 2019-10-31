frutas = ['banana', 'morango', 'melancia']
cesta = []

while True:

    print('(1) para banana')
    print('(2) para morango')
    print('(3) para melancia')
    print('(4) para sair')    

    valor = int(input('Escolha a sua fruta: '))
    
    if valor == 4:
        break
    else:
        cesta.append(frutas[valor - 1])

print('Sua cesta:', cesta)




    
    


