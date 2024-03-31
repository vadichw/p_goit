from collections import Counter

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."


counter = Counter(text)
print(counter)
# def get_count_chars(text):
#     count_dict = {}
#     for i in text:
#         num = count_dict.get(i)
#         if num:
#             count_dict[i] = num + 1
#         else:
#             count_dict[i] = 1
#     print(count_dict)
    
# get_count_chars(text)