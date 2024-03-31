from collections import defaultdict

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

def get_word(text):
    word_list = text.split(' ')
    word_dict = defaultdict(list)
    for i in word_list:
        word_dict[i[0]] = i
    print(word_dict)
get_word(text)
    

# def get_word_list(text):
#     word_list = text.split(' ')
#     word_dict = {}
    
#     for i in word_list:
#         word = word_dict.get(i[0])
#         if word:
#             word.append(i)
#         else:
#             word_dict[i[0]] = [i]
    
#     print(word_dict)

#get_word_list(text)