text = 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor.'
dict_counter = {} # {'L': 1, 'o' : 2} Сколько раз елемент входит в строку
for char in text:
    count = dict_counter.get(char, 0)
    #try:
        #count = dict_counter[char] # Получим значение по ключу
    #except KeyError:
        #count = 0
    count += 1
    dict_counter[char] = count # Записываем значение по ключу
print(dict_counter)


