import pymysql.cursors

try:
    
    conexao = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = '4linux',
        db = '4linux',
        charset = 'utf8mb4',
        cursorclass = pymysql.cursors.DictCursor
    )

except Exception as err:
    
    print('Nao foi possivel conectar com o Banco de Dados')
    print(err)
    
else:
    
    while True:    
    
        with conexao.cursor() as rs:
            
            nome = input('Digite o nome: ')
            nacionalidade = input('Digite a sua nacionalidade: ')
            idade = input('Digite a sua idade: ')
            
            strsql = "INSERT INTO pessoa (nome_pessoa, nacionalidade_pessoa, idade_pessoa) "
            strsql += "VALUES ('" + nome + "', '" + nacionalidade + "', " + idade + ")"
            rs.execute(strsql)
            
            #para alterar algo na base
            conexao.commit()

            strsql = 'SELECT * FROM pessoa'
            rs.execute(strsql)

            for rsX in rs:
                print('--------------------------------------')
                print('ID: ', rsX['id_pessoa'])
                print('Nome: ', rsX['nome_pessoa'])
                print('Nacionalidade: ', rsX['nacionalidade_pessoa'])
                print('Idade: ', rsX['idade_pessoa'])

finally:
    
    conexao.close()
