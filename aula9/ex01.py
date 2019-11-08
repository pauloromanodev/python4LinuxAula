from pymongo import MongoClient

client = MongoClient()

bd = client.pessoa

bd.pessoa.insert_many(
    [
        {
            'nome':'Paulo Cesar',
            'nacionalidade':'Brasileiro',
            'idade': 38
        },
    
        {
            'nome':'John',
            'nacionalidade':'Canadense',
            'idade': 55
        },
        
        {
            'nome':'Katarina',
            'nacionalidade':'Argentina',
            'idade': 22
        },
        
    ] 
)
