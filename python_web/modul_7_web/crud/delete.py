from make_data import User, Article, session

# user = session.get(User, 1)
# session.delete(user)

article = session.get(Article, 1)
session.delete(article)

session.commit()

