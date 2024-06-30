from pymongo import MongoClient


def get_mongo_db():
    client = MongoClient("mongodb+srv://vadich_w:I3wv0Kc9vuy0T96p@cluster0.n7wujvu.mongodb.net/?retryWrites=true&w"
                         "=majority&appName=Cluster0")

    db = client.hw10
    return db
