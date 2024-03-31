import collections

temperature = [0.1, 2.0, 3.0, 4.0, 4.0]
t = [elem + 0.5 for elem in temperature]
print(t)

unique = {elem + 0.5 for elem in temperature}
print(unique)


# LIFO (last in - first out)
from collections import deque
MAX_LEN = 10
lifo = deque(maxlen=MAX_LEN)

def push(element):
    lifo.appendleft(element)
    
def pop():
    return lifo.popleft()

# push('Vadim')
# push('Vika')
# push('Lord')
# push('Hobbit')
# print(lifo)

# name = pop()
# print(name)
# print(lifo)

# FIFO (first in first out)
from collections import deque
MAX_LEN = 10
fifo = deque(maxlen=MAX_LEN)
def push(element):
    fifo.append(element)
def pop():
    return fifo.popleft()

push('Vadim')
push('Vika')
push('Lord')
push('Hobbit')
print(fifo)
name = pop()
print(name)
print(fifo)

from datetime import datetime

# Вернет год и порядковий номер дня

def transform_to_original_date(day, month, year):
    d = datetime(year,month,day).toordinal()
    diff = d - datetime(year, 1, 1).toordinal() + 1 # Щоб рахувати поточний день
    return year, diff

#print(transform_to_original_date(31,12,2023))


# Вводишь порядковий номер дня и год и вернет дату
def trans_to_data(ordinal, year):
    d1 = datetime(year, 1, 1).toordinal()
    return datetime.fromordinal(d1 - 1 + ordinal)

print(trans_to_data(365, 2001))


# написати ф-цію яка визначає день тижня у певної дати у вигляді день-місяць-рік
# days_name = {
#     0: 'Monday',
#     1: 'Tuesday',
#     2: 'Wednesday',
#     3: 'Thursday',
#     4: 'Friday',
#     5: 'Saturday',
#     6: 'Sunday',
# }


import random

start = 'AI'
set_letters = ['A', 'B', 'C', 'D', 'E']
set_numbers = ['0','1','2','3','4','5','6','7','8','9',]

numbers = ''.join(random.choices(set_numbers, k=4))
last_letters = ''.join(random.choices(set_letters, k=2))
# print(numbers)
# print(last_letters)
print(f"{start}{numbers}{last_letters}")


