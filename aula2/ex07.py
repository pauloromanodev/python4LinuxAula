#criar uma lista de 15 numeros e apresentar a soma deles
#com dicionário

dicionario = {
    'nota1':5.5, 
    'nota2':6.5, 
    'nota3':3.5
}

soma = 0

#soma a lista
for i in dicionario.keys():
    soma += dicionario[i]    
    
media = soma / len(dicionario)

#printa
print(media)
    



