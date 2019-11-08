from classes import *

p = Pessoa()

def main():
    
    while True:
    
        ops = {
            '1':p.cadastrarUsuario, 
            '2':p.listarUsuario, 
            '3':p.alterarUsuario, 
            '4':p.apagarUsuario,             
            '5':exit
        
        }

        opcao = input(
                  '-----------------------\n'
                  '1. Cadastrar Usuario\n' +
                  '2. Listar Usuario\n' +
                  '3. Alterar Usuarios\n' +
                  '4. Apagar Usuario\n' +                  
                  '5. Sair\n'
                  '-----------------------'
                  )    
    
        ops[opcao]()
    
if __name__ == '__main__':
    main()
