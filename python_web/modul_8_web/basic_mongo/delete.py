from bson.objectid import ObjectId

from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient(
    "mongodb+srv://vadich_w:I3wv0Kc9vuy0T96p@cluster0.n7wujvu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    server_api=ServerApi('1')
)
db = client.book

db.cats.delete_one({"name": "Liza"})
result = db.cats.find_one({"name": "Liza"})
print(result)
