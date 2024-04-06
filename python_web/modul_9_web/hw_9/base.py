import pymongo
from main import quotes, authors

# Підключення до MongoDB
client = pymongo.MongoClient("mongodb+srv://vadich_w:I3wv0Kc9vuy0T96p@cluster0.n7wujvu.mongodb.net/?retryWrites=true"
                             "&w=majority&appName=Cluster0")
db = client["hw9"]
quotes_collection = db["quotes"]
authors_collection = db["authors"]

# Збереження цитат у колекцію
for quote in quotes:
    quotes_collection.insert_one(quote)

# Збереження авторів у колекцію

for author_name in authors:
    author_doc = {"name": author_name}  # Створюємо словник з іменем автора
    authors_collection.insert_one(author_doc)

print("Дані збережено у базу даних MongoDB.")
