articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key, letter_case=False):

    matching_articles = []
    search_key = key.lower() if not letter_case else key
    
    for article in articles_dict:
        author = article['author'].lower() if not letter_case else article['author']
        title = article['title'].lower() if not letter_case else article['title']
        if author.find(search_key) != -1 or title.find(search_key) != -1:
            matching_articles.append({
                'author': article['author'],
                'title': article['title'],
                'year': article['year']
            })
    return matching_articles

####

def find_articles_1(articles_dict, key, letter_case=False):
    results = []
    for article in articles_dict:
        author = article['author']
        title = article['title']
        year = article['year']
        
        if not letter_case:
            # Якщо letter_case=False, перетворюємо ключ та статтю в нижній регістр для порівняння
            key_lower = key.lower()
            author_lower = author.lower()
            title_lower = title.lower()
        else:
            key_lower = key
            author_lower = author
            title_lower = title
        
        # Перевіряємо, чи містить ключ частинку у назві або імені автора
        if key_lower in author_lower or key_lower in title_lower:
            results.append({'author': author, 'title': title, 'year': year})
    
    return results
