from bson.objectid import ObjectId

from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient(
    "mongodb+srv://vadich_w:I3wv0Kc9vuy0T96p@cluster0.n7wujvu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    server_api=ServerApi('1')
)

db = client.book

# Достать один документ find_one
# result = db.cats.find_one({"_id": ObjectId("60d24b783733b1ae668d4a77")})
# print(result)

# Достать несколько документов
result = db.cats.find({})
for el in result:
    print(el)
