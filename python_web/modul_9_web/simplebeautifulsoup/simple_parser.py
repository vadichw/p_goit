import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')

for quote in quotes:
    print(quote.text)

for author in authors:
    print(author.text)

# Додамо код отримання всіх тегів для кожної цитати. Спочатку потрібно отримати кожен зовнішній блок кожної колекції
# тегів. Якщо цей перший крок не виконати, теги можна буде отримати, але асоціювати їх із конкретною цитатою — ні.
#
# Коли блок отримано, можна опускатись нижче за допомогою функції find_all для отриманої підмножини. А далі буде
# потрібно додати внутрішній цикл для завершення процесу.

tags = soup.find_all('div', class_='tags')

for i in range(0, len(quotes)):
    print(quotes[i].text)
    print('--' + authors[i].text)
    tagsforquote = tags[i].find_all('a', class_='tag')
    for tagforquote in tagsforquote:
        print(tagforquote.text)
    break # если надо все цитаты и авторы, и теги, то убираем брейк


