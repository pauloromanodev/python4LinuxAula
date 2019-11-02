from func import *

def main():

    while True:
        
        print('1. Cadastrar pessoa')
        print('2. Consultar pessoa')
        print('3. Sair')
    
        op = input('Digite sua opção:')
        
        if op == '1':
            cpf = input('Digite o CPF:')
            nome = input('Digite o Nome:')
            email = input('Digite o E-mail:')
            uf = input('Digite a UF:')
            
            cadastrar(cpf, nome, email, uf)            
            
        if op == '2':
            cpf = input('Digite o CPF:')
            
            consultar(cpf)
            
        if op == '3':
            break        
    
if __name__ == '__main__':
    main()
