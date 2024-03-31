import requests
from bs4 import BeautifulSoup
from modul_9.simplebeautifulsoup.search_elements import first_paragraph

url = "http://quotes.toscrape.com/"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

# отримати текст першого тега <p> на сторінці
first_paragraph_text = first_paragraph.get_text()
# print(first_paragraph_text.strip())  # 'Login'

# отримати значення атрибута "href" першого тегу <a> на сторінці
first_link = soup.find("a")
first_link_href = first_link["href"]
print(first_link_href)  # '/'

