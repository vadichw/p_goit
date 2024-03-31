import re

def replace_spam_words(text, spam_words):
    for bad_word in spam_words:
        pattern = re.compile(r'\b{}\b'.format(re.escape(bad_word)), re.IGNORECASE)
        text = pattern.sub('*' * len(bad_word), text)

    return text