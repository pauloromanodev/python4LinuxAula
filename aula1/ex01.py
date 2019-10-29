#calculadora

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
operacao = input('Escolha a operação: ')

if operacao == '+':
    resultado = num1 + num2
    
elif operacao == '-':
    resultado = num1 - num2
    
elif operacao == '/':
    resultado = num1 / num2
    
elif operacao == '*':
    resultado = num1 * num2

print('O resultado é: {0:.2f}'.format(resultado))

exit()

#script de saudação

nome = input('Digite o seu nome: ')
sobrenome = input('Digite o seu sobrenome: ')

print('Olá meu nome é', nome, sobrenome)
