cesta = []

def mostra_menu():
    print('(1) para banana')
    print('(2) para morango')
    print('(3) para melancia')
    print('(4) para sair')
    
def mostra_menu_invalido():
    print('--------------') 
    print('Opção inválida') 
    print('--------------') 
    
def recebe_valor():
    val = int(input('Escolha a sua fruta: '))
    return val
    
def mostra_resultado(total):
    print('Sua cesta:', total)
    
def soma_cesta(cesta):
    
    soma = 0
    
    for i in cesta:
        soma += i
        
    return soma
    
def adiciona_fruta(fruta):    
    cesta.append(fruta)
    

    
    

    
    
    

