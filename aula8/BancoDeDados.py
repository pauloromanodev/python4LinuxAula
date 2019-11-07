import pymysql.cursors

class Conexao:
    
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password = '4linux'
        self.banco = '4linux'
        self.charset = 'utf8mb4'
        self.conexao = ''        
        
    def abre_conexao(self):
        try:
            self.conexao = pymysql.connect(
                host = self.host,                
                user = self.user,
                password = self.password,
                db = self.banco,
                charset = self.charset,
                cursorclass = pymysql.cursors.DictCursor)

        except Exception as err:
            
            print('Nao foi possivel conectar com o Banco de Dados')
            print(err)
            
            
    def executaSql(self, strsql):
        with self.conexao.cursor() as cursor:
            cursor.execute(strsql)
            self.conexao.commit()
            return cursor
            
    def fecha_conexao(self):
        self.conexao.close()
