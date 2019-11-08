from BancoDeDados import *

db = Conexao()
db.abre_conexao()

strsql = 'SELECT * FROM pessoa'

rs = db.executaSql(strsql)

for rsX in rs:
    print('--------------------------------------')
    print('ID: ', rsX['id_pessoa'])
    print('Nome: ', rsX['nome_pessoa'])
    print('Nacionalidade: ', rsX['nacionalidade_pessoa'])
    print('Idade: ', rsX['idade_pessoa'])

db.fecha_conexao()
