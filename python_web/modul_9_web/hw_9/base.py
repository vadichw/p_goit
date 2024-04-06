import pymongo
from main import quotes, authors

client = pymongo.MongoClient("mongodb+srv://vadich_w:I3wv0Kc9vuy0T96p@cluster0.n7wujvu.mongodb.net/?retryWrites=true"
                             "&w=majority&appName=Cluster0")
db = client["hw9"]
quotes_collection = db["quotes"]
authors_collection = db["authors"]

for quote in quotes:
    quotes_collection.insert_one(quote)

for author_name in authors:
    author_doc = {"name": author_name}
    authors_collection.insert_one(author_doc)

print("Data is saved to database")
