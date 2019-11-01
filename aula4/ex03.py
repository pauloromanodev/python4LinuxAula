from ex03_func import *

frutas = {
    'banana': 1.50, 
    'morango': 3.99, 
    'melancia': 5.00
}

while True:

    mostra_menu()
    valor = recebe_valor()
    
    if valor == 4:
        break        
    elif valor == 1:
        adiciona_fruta(frutas['banana'])        
    elif valor == 2:
        adiciona_fruta(frutas['morango'])        
    elif valor == 3:
        adiciona_fruta(frutas['melancia'])        
    else:
        mostra_menu_invalido()

soma = soma_cesta(cesta)
mostra_resultado(soma)
