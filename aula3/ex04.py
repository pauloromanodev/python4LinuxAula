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
    dic = {'+':soma, '-':subt, '*':mult, '/':soma}
    
    v1 = float(input('Digite o primeiro valor:'))
    v2 = float(input('Digite o segundo valor:'))
    op = input('Digite a operação (+, -, *, /):')
    
    print(dic[op](v1,v2))
    
if __name__ == '__main__':
    main()

