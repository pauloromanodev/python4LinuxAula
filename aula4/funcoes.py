
def soma(*numeros):
    
    resultado = 0
    
    for num in numeros:
        resultado += num
        
    return resultado

    
def sub(*numeros):
    
    resultado = 0
    
    for num in numeros:
        resultado -= num
        
    return resultado


def mult(*numeros):
    
    resultado = 0
    
    for num in numeros:
        resultado *= num
        
    return resultado


def div(*numeros):
    
    resultado = 0
    
    for num in numeros:
        resultado /= num
        
    return resultado
    
