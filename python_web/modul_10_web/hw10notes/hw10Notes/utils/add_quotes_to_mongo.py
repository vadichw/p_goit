import json
from bson.objectid import ObjectId

from pymongo import MongoClient

client = MongoClient("mongodb+srv://vadich_w:I3wv0Kc9vuy0T96p@cluster0.n7wujvu.mongodb.net/?retryWrites=true&w"
                     "=majority&appName=Cluster0")
db = client.hw10

with open('quotes.json', 'r', encoding='utf-8') as file:
    quotes = json.load(file)

for quote in quotes:
    author = db.authors.find_one({'fullname': quote['author']})
    if author:
        db.quotes.insert_one({
            'quote': quote['quote'],
            'tags': quote['tags'],
            'author': ObjectId(author['_id'])
        })
