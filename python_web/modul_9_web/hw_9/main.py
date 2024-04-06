import requests
from bs4 import BeautifulSoup
import json


def scrape_quotes(url):
    quotes = []
    authors = []
    while url:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        for quote in soup.select('div.quote'):

            text = quote.select_one('span.text').get_text()
            author = quote.select_one('small.author').get_text()
            authors.append(author)
            tags = [tag.get_text() for tag in quote.select('a.tag')]
            quotes.append({'text': text, 'author': author, 'tags': tags})

        next_page = soup.select_one('li.next > a')
        url = next_page['href'] if next_page else None
        if url and not url.startswith('http'):
            url = f'http://quotes.toscrape.com{url}'

    return quotes, list(authors)


def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


quotes, authors = scrape_quotes("http://quotes.toscrape.com/")

save_to_json(quotes, 'quotes.json')
save_to_json(authors, 'authors.json')

print("The files were created and saved")
