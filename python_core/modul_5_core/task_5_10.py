import re
from pprint import pprint

def find_word(text, word):
    needed_word = re.compile(r'\b{}\b'.format(re.escape(word)))
    needed_text = needed_word.search(text)

    result_dict = {
        'result': bool(needed_text),
        'first_index': needed_text.start() if needed_text else None,
        'last_index': needed_text.end() if needed_text else None,
        'search_string': word,
        'string': text
    }

    return result_dict

pprint((find_word("Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.", "python")))