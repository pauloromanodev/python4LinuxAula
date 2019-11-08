from pymongo import MongoClient

client = MongoClient()

bd = client.pessoa

for registro in bd.pessoa.find():
    print(registro)
    
print(bd.pessoa.find({'nome':'John'}))
