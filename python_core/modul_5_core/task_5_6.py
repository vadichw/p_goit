def is_spam_words(text, spam_words, space_around = False):
    text = text.lower()
    text_list = text.split(' ')
    for spam_word in spam_words:
        if not space_around:
            if spam_word in text:
                return True
            break
        
        for text_str in text_list:
            if spam_word not in text_str:
                continue
            if (text_str == spam_word) or (text_str == spam_word + '.'):
                return True
    return False
    
