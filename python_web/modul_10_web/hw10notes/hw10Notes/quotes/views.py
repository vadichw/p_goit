from django.shortcuts import render
from .utils import get_mongo_db
from django.core.paginator import Paginator


def main(request, page=1):
    db = get_mongo_db()
    quotes = db.quotes.find()
    per_page = 2
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})
