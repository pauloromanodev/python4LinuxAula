from pymongo import MongoClient

client = MongoClient()

bd = client.pessoa

bd.pessoa.update_one({'nome':'John'}, {'$set': {'nome':'Steve', 'idade': 26}})
