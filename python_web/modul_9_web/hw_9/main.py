import requests
import json
from bs4 import BeautifulSoup


# Функція для отримання даних зі сторінки
def scrape_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup


# Функція для отримання цитат зі сторінки
def get_quotes(page_soup):
    quotes = []
    for quote in page_soup.select('.quote'):
        text = quote.select_one('.text').get_text()
        author = quote.select_one('.author').get_text()
        tags = [tag.get_text() for tag in quote.select('.tag')]
        quotes.append({'text': text, 'author': author, 'tags': tags})
    return quotes


# Функція для отримання URL наступної сторінки
def get_next_page_url(page_soup):
    next_page_link = page_soup.select_one('.next > a')
    if next_page_link:
        return base_url + next_page_link['href']  # Зміна тут
    else:
        return None

# Спочатку визначимо базовий URL та список для зберігання цитат
base_url = 'http://quotes.toscrape.com'
all_quotes = []

# Скрапінг та збереження даних усіх сторінок
current_page_url = base_url
while current_page_url:
    page_soup = scrape_page(current_page_url)
    all_quotes.extend(get_quotes(page_soup))
    current_page_url = get_next_page_url(page_soup)


# Зберігання цитат у файл quotes.json
with open('quotes.json', 'w') as f:
    json.dump(all_quotes, f, indent=2)

# Збереження авторів у файл authors.json
authors = list(set(quote['author'] for quote in all_quotes))
authors_data = [{'author': author} for author in authors]
with open('authors.json', 'w') as f:
    json.dump(authors_data, f, indent=2)
