from pymongo import MongoClient
import json

# З'єднання з базою даних MongoDB (встановіть ваші власні дані)
client = MongoClient('mongodb+srv://vadich_w:I3wv0Kc9vuy0T96p@cluster0.n7wujvu.mongodb.net/?retryWrites=true&w'
                     '=majority&appName=Cluster0')

# Вибір або створення колекції для цитат та авторів
db = client['mydatabase']
quotes_collection = db['quotes']
authors_collection = db['authors']

# Завантаження даних з файлів у базу даних
with open('quotes.json') as f:
    quotes_data = json.load(f)
quotes_collection.insert_many(quotes_data)

with open('authors.json') as f:
    authors_data = json.load(f)
authors_collection.insert_many(authors_data)

# Перевірка, що дані були успішно завантажені
print(quotes_collection.count_documents({}))  # Повинно вивести кількість цитат
print(authors_collection.count_documents({}))  # Повинно вивести кількість авторів
