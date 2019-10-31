frutas = {
    'banana': 1.50, 
    'morango': 3.99, 
    'melancia': 5.00
}

cesta = []
total = 0

while True:

    print('(1) para banana')
    print('(2) para morango')
    print('(3) para melancia')
    print('(4) para sair')    

    valor = int(input('Escolha a sua fruta: '))
    
    if valor == 4:
        break
        
    elif valor == 1:
        cesta.append(frutas['banana'])
        
    elif valor == 2:
        cesta.append(frutas['morango'])
        
    elif valor == 3:
        cesta.append(frutas['melancia'])
        
    else:
        print('--------------') 
        print('Opção inválida') 
        print('--------------') 

for i in cesta:
    total += i

print('Sua cesta:', total)





    
    


