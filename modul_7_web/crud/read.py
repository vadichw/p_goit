from make_data import User, Article, session

person = session.query(User).all()

for p in person:
    print(p.id, p.name)

article = session.query(Article).all()

for a in article:
    print(f"Author: {a.author}\n Title: {a.title}\n Content: {a.content}\n")


