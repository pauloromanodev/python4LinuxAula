def soma(v1,v2):
    return v1 + v2    
    
def subt(v1,v2):
    return v1 - v2    
    
def mult(v1,v2):
    return v1 * v2    
    
def divi(v1,v2):
    if v2 != 0:
        return v1 / v2
    else:
        return 'Não é possível dividir por zero.'
        
def main():

    while True:
    
        res = 0
        
        v1 = float(input('Digite o primeiro valor:'))
        v2 = float(input('Digite o segundo valor:'))
        op = input('Digite a operação (+, -, *, /):')

        if op == '+':
            res = soma(v1,v2)
            
        if op == '-':
            res = subt(v1,v2)
            
        if op == '*':
            res = mult(v1,v2)
            
        if op == '/':
            res = divi(v1,v2)            
        
        print('O resultado é:', res)
    
if __name__ == '__main__':
    main()
