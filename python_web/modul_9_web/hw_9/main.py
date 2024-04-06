import requests
from bs4 import BeautifulSoup
import json


# Функція для отримання даних про цитати
def scrape_quotes(url):
    quotes = []
    authors = set()
    while url:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        for quote in soup.select('div.quote'):
            text = quote.select_one('span.text').get_text()
            author = quote.select_one('small.author').get_text()
            authors.add(author)
            tags = [tag.get_text() for tag in quote.select('a.tag')]
            quotes.append({'text': text, 'author': author, 'tags': tags})
        next_page = soup.select_one('li.next > a')
        url = next_page['href'] if next_page else None
        if url and not url.startswith('http'):
            url = f'http://quotes.toscrape.com{url}'  # Повний URL для наступної сторінки
    return quotes, list(authors)


# Функція для збереження даних у JSON-файл
def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


# Отримання цитат та авторів
quotes, authors = scrape_quotes("http://quotes.toscrape.com/")
# Збереження цитат та авторів у JSON-файли
save_to_json(quotes, 'quotes.json')
save_to_json(authors, 'authors.json')
