import json
from models import Author, Quote
import connect


def search_quotes(command):
    parts = command.split(':')
    if len(parts) != 2:
        return "Невірний формат команди. Формат: команда:значення"

    action, value = parts
    if action == 'name':
        author = Author.objects(fullname=value).first()  # Виправлено тут
        if author:
            quotes = Quote.objects(author=author)
            return [quote.quote for quote in quotes]  # Виправлено тут
        else:
            return "Автор не знайдений."
    elif action == 'tag':
        quotes = Quote.objects(tags=value)
        return [quote.quote for quote in quotes]  # Виправлено тут
    elif action == 'tags':
        tags = value.split(',')
        quotes = Quote.objects(tags__contains=tags)
        return [quote.quote for quote in quotes]

    elif action == 'exit':
        exit()
    else:
        return "Невідома команда."


if __name__ == "__main__":
    while True:
        command = input("Введіть команду: ").strip()
        result = search_quotes(command)
        if result:
            if isinstance(result, list):
                for quote in result:
                    print(quote)
            else:
                print(result)
