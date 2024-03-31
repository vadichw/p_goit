#------------------ THE LISTS----------------#

# CLEAR()
num = [1,2,3]
print(num)
num.clear()
print(num)

# EXTEND
num = [1,2,3]
char = ["a", "b", "c"]
num.extend(char)
print(num)

# FIND INDEX()
chars = ['a', 'b', 'c', 'd']
c_ind = chars.index('d')
print(c_ind)

#COUNT()
chars = ['a', 'b', 'c', 'a']
ch_a = chars.count('a')
print(ch_a)

#COPY()
chars =  ['a', 'b']
cop = chars.copy()
print(cop)


#----------------Dictionary--------------------#

# pop(key) — повертає значення елементу і видаляє пару ключ-значення зі словника

chars = {'a': 1, 
         'b': 2,}
b_ch = chars.pop('b')
print(b_ch)
print(chars)

# update(another_dict) — розширює словник значеннями з іншого словника
chars = {'a': 1, 'b': 2}
chars.update({"c": 3})
print(chars)

# get(key[, default]) — не викликає виключення, якщо ключа немає в словнику, повертає default, за замовчуванням default=None
chars = {'a': 1, 'b': 2}
c_idx = chars.get('c', -1)
print(c_idx)

# keys(), value()

num = {
    1: "one",
    2: "two",
    3: "three",
}

for n in num.keys():
    print(n)

for nv in num.values():
    print(nv)

for key, value in num.items():
    print(key, value)

# n.key, n.values, n.items
a = {"key": 1, "key2" : 2}
print(a.keys())
print(a.values())
print(a.items())

#-----------SET----------------------#

#Множини — це неврегульований контейнер, який містить тільки унікальні елементи. У множину можна додавати тільки незмінні типи даних.

#Унікальність має на увазі, що якщо множина вже містить такий елемент, то спроба додати ще один такий самий нічого не змінить.

a = set("hello")
print(a)
# or
a = {"hello"} # it`s a set

# add()
numbers = {1, 2, 3}
numbers.add(4)
print(numbers) 

#remove()
numbers = {1, 2, 3}
numbers.remove(3)
print(numbers)

# discard(elem) — видаляє елемент з множини і не викликає виняток, якщо його немає

numbers = {1, 2, 3}
numbers.discard(2)
print(numbers) 

###

a = set('hello')
print(a)

b = set('hi there!')
print(b)

# Щоб знайти загальні елементи для двох множин, виконаємо над ними операцію &
print(a&b)

# Знайдемо усі елементи з двох множин, окрім загальних, за допомогою оператора ^
print(a^b)

# Об'єднання множин, або просто усі елементи з обох множин знаходяться за допомогою оператора |
print(a|b)

# STRINGS

#Щоб перевірити, що рядок починається з підрядка, є метод startswith:

s = "Bill Jons"
print(s.startswith("Bi"))

# Щоб перевірити, що рядок закінчується підрядком, використовується метод endswith:

s = "hello.jpg"
print(s.endswith("jpg"))


#------------Os PathLib------------------------------#

import os
#path = os.path.join("user", "folder", "slak") # Create path
#print(path)

#fol = os.makedirs("user/bin/media") # Create folder 
#print(fol)

#import glob
#print(glob.glob("m*")) # Найдет файлы, которые начинаються на m


from pathlib import*
current_dir = Path.cwd()
print(current_dir)

home_dir = Path.home()
print(home_dir)

f = Path.cwd() / 'user' / 'folder'
print(f)