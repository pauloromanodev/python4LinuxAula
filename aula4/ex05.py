#arquivos

nome = input('Digite o seu nome:')
idade = int(input('Digite a sua idade:'))
cpf = input('Digite o seu CPF:')
    
conteudo = nome + ';' + str(idade) + ';' + cpf + ';'

print(conteudo)

with open('arquivo.txt', 'w') as f:
    f.write(conteudo)


    
