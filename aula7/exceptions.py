while True:

    try:
        #bloco de tentativa
        opcao = int(input('Escolha a opcao: '))
    #except ValueError as err:
    except Exception as err:
        #print(err)    
        print('Digite apesar numeros.', err)
        
    finally: #opcional
        print('')
    
    

