# Початок гіперпосилання може бути http:// або https://

# доменне ім'я — це набір латинських букв, цифр, символів підкреслення _ та точок .

# символи точок . не можуть зустрічатися поруч

import re

def find_all_links(text):
    result = []
    iterator = re.finditer(r'https?://(?:[\w_]+\.)*[\w_]+\.\w+', text)
    #iterator = re.finditer(r'(https?|ftp):\/\/[^\s/$.?#].[^\s]*', text) НЕПРАВИЛЬНИЙ ВАРИАНТ
    for match in iterator:
        result.append(match.group())
    return result

print(find_all_links('The main search site in the world is https://www.google.com The main social network for people in the world is https://www.facebook.com But programmers have their own social network http://github.com There they share their code. some url to check https://www..facebook.com www.facebook.com'))