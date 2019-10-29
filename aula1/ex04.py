ano = int(input('Digite o ano do seu aniversário: '))

if ano <= 1964:
    resultado = 'BBoomer'
    
elif ano > 1964 and ano <= 1981:
    resultado = 'Geração X'
    
elif ano > 1981 and ano <= 1996:
    resultado = 'Geração Y'
    
elif ano > 1996:
    resultado = 'Geração Z'
    

print(resultado)
