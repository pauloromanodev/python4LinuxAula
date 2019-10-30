frase = '4 linux open software specialists'
vogais = 'aeiou'

conta_vogal = 0

for letra in frase:
    if letra in vogais:
        conta_vogal += 1

print('A frase tem', conta_vogal, 'vogais')
        
