from BancoDeDados import *

class Pessoa():
    
    def __init__(self):
        self.nome = ''
        self.nacionalidade = ''
        self.idade = 0        
        
        
        
    
    def cadastrarUsuario(self):
        
        nome = input('Digite o nome: ')
        nacionalidade = input('Digite a sua nacionalidade: ')
        idade = input('Digite a sua idade: ')
        
        #valida se todos os campos foram preenchidos
        if len(nome) > 0 and len(nacionalidade) > 0 and len(idade) > 0:
            
            strsql = "INSERT INTO pessoa (nome_pessoa, nacionalidade_pessoa, idade_pessoa) "
            strsql += "VALUES ('" + nome + "', '" + nacionalidade + "', " + idade + ")"
            
            db = Conexao()
            db.abre_conexao()
            
            rs = db.executaSql(strsql)
            
            db.fecha_conexao()
            
            print('-------------------------------')
            print('Cadastro realizado com sucesso!')
            print('-------------------------------')
            
        else:
            
            print('--------------------------------------')
            print('Todos os campos devem ser preenchidos.')
            print('--------------------------------------')



    
    def listarUsuario(self):
        
        strsql = 'SELECT * FROM pessoa'
        
        db = Conexao()
        db.abre_conexao()

        rs = db.executaSql(strsql)
        
        for rsX in rs:
            print('--------------------------------------')
            print('ID: ', rsX['id_pessoa'])
            print('Nome: ', rsX['nome_pessoa'])
            print('Nacionalidade: ', rsX['nacionalidade_pessoa'])
            print('Idade: ', rsX['idade_pessoa'])

        db.fecha_conexao()
        
        
        
        
    def alterarUsuario(self):
        id_pessoa = input('Digite o ID do usuario: ')
        
        #valida se o ID foi digitado
        if len(id_pessoa) > 0:
            
            nome = input('Digite o nome do usuario: ')
            nacionalidade = input('Digite a nacionalidade do usuario: ')
            idade = input('Digite a idade do usuario: ')
            
            strsql = "UPDATE pessoa SET nome_pessoa = '" + nome + "', nacionalidade_pessoa = '" + nacionalidade + "', idade_pessoa = " + idade + " where id_pessoa = " + id_pessoa
            
            
            try:
    
                db = Conexao()
                db.abre_conexao()
                
                rs = db.executaSql(strsql)
                
                db.fecha_conexao()
                print('-----------------------------')
                print('Registro apagado com sucesso!')
                print('-----------------------------')

            except Exception as err:
                
                print('------------------------------')
                print('O ID é invalido ou nao existe.')
                print('------------------------------')
                print(err)
                
                
                
        
    def apagarUsuario(self):
        id_pessoa = input('Digite o ID do usuario: ')        
        
        #valida se o ID foi digitado
        if len(id_pessoa) > 0:
            
            strsql = "DELETE FROM pessoa WHERE id_pessoa = " + id_pessoa
            
            print(strsql)
            
            try:
            
                db = Conexao()
                db.abre_conexao()
                
                rs = db.executaSql(strsql)
                
                db.fecha_conexao()
                
                print('------------------------------')
                print('Registro alterado com sucesso!')
                print('------------------------------')
            
            except Exception as err:
                
                print('------------------------------')
                print('O ID é invalido ou nao existe.')
                print('------------------------------')
                print(err)
