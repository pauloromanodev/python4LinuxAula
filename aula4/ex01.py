#!/usr/bin/python3

#parâmetros em funções

def soma(lista):
    resultado = 0
    for num in lista:
        resultado += num
    return resultado
    
def main():
    numeros = [1, 2, 3, 4, 5]
    
    print(soma(numeros))
    
if __name__ == '__main__':
    main()
