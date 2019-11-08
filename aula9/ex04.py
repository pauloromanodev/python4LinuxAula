from pymongo import MongoClient

client = MongoClient()

bd = client.pessoa

bd.pessoa.delete_one({'nome':'Paulo Cesar'})
