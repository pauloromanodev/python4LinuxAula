#arquivos

with open('arquivo.txt', 'r') as f:
    conteudo = f.read()
    
print(conteudo)

conteudo += 'teste'

with open('arquivo.txt', 'w') as f:
    f.write(conteudo)

    
