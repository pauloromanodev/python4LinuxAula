
idade = int(input('Digite a sua idade: '))
habilitacao = input('Possui CNH? (S/N)')

if (idade >= 18 and habilitacao == 'S'):    
    print('Pode dirigir')
else:
    print('Não possui habilitação ou não tem idade mínima')


