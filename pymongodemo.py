from pymongo import MongoClient

client = MongoClient()
client = MongoClient('localhost', 27017)
db = client['NewDB']
col_ModeS_Long = db['ModeS_Long']
col_ModeS_Long.insert_one({"name":"Titas",'age':23, "company":"asl"})