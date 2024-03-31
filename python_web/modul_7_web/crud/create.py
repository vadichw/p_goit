from make_data import User, Article, session

person = User(name='Vadim')


article = Article(title='The best woman',
                  content='This article...',
                  author=person)
session.add(person, article)
session.commit()





