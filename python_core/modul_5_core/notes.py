#\n Перенесення рядка - переносить на новий рядок
#\f	Перенесення сторінки
#\r	Повернення каретки
#\t	Горизонтальна табуляція
#\v	Вертикальна табуляція

jingle_bells = "Jingle bells, jingle bells\nJingle all the way\nOh, what fun it is to ride\nIn a one horse open sleigh"

print(jingle_bells)

###-------------------------String Methogs-------------###

# find()
# Повертає -1, якщо послідовність не знайдена.
# Цей метод виводить індекс початку першого збігу в рядку s, починаючи з start до end. Якщо start та end не вказані, то з початку і до кінця 
# Поиск идет СЛЕВА

s = "Hi there!"

#start = 0
#end = 7

print(s.find("er")) 
print(s.find("A"))
#index()
print(s.index("h"))

#Можно искать СПРАВА
word = 'some word'
print(word.rfind('d'))
print(word.rindex("d"))

### SPLIT ###
#Для такого завдання можна скористатися методом split, який приймає як аргумент підрядок-маркер, який буде межею, по якій потрібно розбити рядок на частини. В результаті виклику повертається список рядків.

s = "I am learning strings in Python. Some new methods got now."
sentence = s.split('. ')
print(sentence[0])
print(sentence[1])

# Удалает пробелы (strip, rstrip, lstrip)
clean = '   spacious   '.strip()
print(clean)

# replace()
dogs_text = "All dogs bark like dogs."
cats_text = dogs_text.replace("dogs", "cats")
print(dogs_text)
print(cats_text)

# Для видалення фіксованої послідовності НА ПОЧАТКУ рядка є метод removeprefix
print('TestHook'.removeprefix('Test'))
print('TestHook'.removeprefix('Hook')) # Не удалил, ибо ХУК в конце

# Є парний метод для видалення послідовності в кінці рядка, removesuffix
print('TestHook'.removesuffix('Hook'))
print('TestHook'.removesuffix('Test'))

# TRANSLATE
# В рядках є метод translate, цей метод дозволяє замінити символ в рядку на інший з мапи відповідності, яку можна задати.
map = {ord('з'): 'z', ord('ю'): 'u'}
translate = 'зю'.translate(map)
print(translate)

name_1 = {ord('В'): 'V',
          ord('а'): 'a',
           ord('д') : 'd',
            ord('и') : 'i',
             ord('м') : 'm', }
name = 'Вадим'.translate(name_1)
print(name)

# 
###
txt = "sun"
my_table = txt.maketrans("u", "o")
print(txt.translate(my_table)) # son

txt = "sun"
my_table = txt.maketrans("nus", "mot")
print(txt.translate(my_table))  # tom

# Третій параметр у таблиці зіставлення описує символи, які ви хочете видалити з рядка:
txt = "the sun"
my_table = txt.maketrans("nus", "nos", "he t")
print(txt.translate(my_table))  # son


# Якщо ми збираємося транслювати кирилицю на латиницю, у нас може виникнути проблема, наприклад, при транслітерації слова "чаша", яке має бути "chasha" і має довжину на два символи більше. Використання maketrans викличе помилку. Як бути?

# Для цього можна використовувати вбудовану функцію zip, яка перетворює численні об'єкти, що ітеруються в єдиний об'єкт кортежів, що ітерується, та складається з відповідних елементів

CYRILLIC = ("а", "ч", "ш")
LATIN = ("a", "ch", "sh")

TRANSLIT_DICT = {}

for c, l in zip(CYRILLIC, LATIN):
    TRANSLIT_DICT[ord(c)] = l
    TRANSLIT_DICT[ord(c.upper())] = l.upper()

print("чаша".translate(TRANSLIT_DICT))  # chasha
print("ЧАША".translate(TRANSLIT_DICT))  # CHASHA

##Наприклад, вивести числа від 1 до 15 в десятковому, шістнадцятковому, вісімковому і двійковому представленні:
for i in range(5):
    s = "int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(i)
    print(s)

# Або вивести квадрати та куби чисел до 12 у вигляді таблиці, відцентрувавши значення у стовпцях по 10 символів шириною:
width = 5
for num in range(12):
    print('{:^10} {:^10} {:^10}'.format(num, num**2, num**3))


s = "{name} {last_name}".format(last_name = "Dilan", name = "Bob")
s1 ="{name!r} {last_name!s}".format(last_name = "Marly", name = "Bob")
print(s)
print(s1)

# Регулярні вирази
# Наприклад, \d задає будь-яку цифру, а \d+ — задає будь-яку послідовність з однієї або більше цифр.
import re
s = "I am 22 years old and"
age = re.search('\d+', s)
age_1 = re.search('\d+', s)
print(age_1.group())
print(age)

# findall()
# Коли потрібно знайти всі відповідні шаблону значення, можна скористатися функцією findall.
s = "I bought 7 nuts for 6$ and 10 bolts for 3$."
num = re.findall('\d+', s)
print(num)

# sub()
# Щоб замінити всі підрядки, що відповідають регулярному виразу, можна скористатися функцією sub.
p = re.sub(r'(blue|white|red)', 'colour', 'blue socks and red shoes')
print(p)


