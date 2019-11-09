#apis

import requests 
import time


cep = input('Digite o CEP:')

#https://viacep.com.br/ws/03191140/json

destino = 'https://viacep.com.br/ws/' + cep + '/json'

resposta = requests.get(destino)

if resposta.status_code == 200:
    json = resposta.json()

    #print('CEP:', json['cep'])
    #print('Logradouro:', json['logradouro'])
    #print('Bairro:', json['bairro'])
    
    print(json)
