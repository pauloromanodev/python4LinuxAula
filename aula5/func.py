def cadastrar(cpf, nome, email, uf):
    
    conteudo = cpf + ';' + nome + ';' + email + ';' + uf + '\n'
    
    with open('arquivo.txt', 'a') as f:
        f.write(conteudo)
    
    print('---------------------------')
    print('Registro salvo com sucesso!')
    print('---------------------------')
    
def consultar(cpf):
    
    with open('arquivo.txt', 'r') as f:
        conteudo = f.readlines()
 
    for valor in conteudo:        
        if cpf in valor:  
            saida = valor.split(';')
            print('O CPF é:', saida[0])
            print('O nome é:', saida[1])
            print('O email é:', saida[2])
            print('O uf é:', saida[3])
    else:
        print('registro não encontrado')
    
            
