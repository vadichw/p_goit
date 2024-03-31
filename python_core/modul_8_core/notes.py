from datetime import datetime, timedelta

current_date_time = datetime.now()

print(current_date_time.date())
print(current_date_time.time())


print(current_date_time)
print(current_date_time.year)       
print(current_date_time.month)       
print(current_date_time.day)         
print(current_date_time.hour)        
print(current_date_time.minute)      
print(current_date_time.second)      
print(current_date_time.microsecond) 

# Create a date
d1 = datetime(year=2023, month=11, day=24, hour=9)
print(d1)

# 0 - Monday, 1- Tuesday...
seventh_day_2020 = datetime(year=2002, month=5, day=14, hour=10)
print(seventh_day_2020.weekday())

# Сравнения дат
current_datetime = datetime.now()
future_month = (current_datetime.month % 12) + 1
future_year = current_datetime.year + int(current_datetime.month / 12)
future_datetime = datetime(future_year, future_month, 1)
print(current_datetime < future_datetime)


day_2019 = datetime(year=2019, month=9, day=4, hour=3)
day_2020 = datetime(year=2020, month=7, day=3, hour=8)
difference = day_2020 - day_2019
# В результате получаем объект timedelta
print(difference)


# Об'єкти timedelta можна створювати самостійно, щоб отримати дату/час віддалену від початкової:
day_2020 = datetime(year=2020, month=4, day=2, hour=4)
four_weeks_interval = timedelta(weeks=4)

print(day_2020 - four_weeks_interval)
print(day_2020 + four_weeks_interval)

# Об'єкт timedelta можна створити, задаючи тижні, дні, години, хвилини, секунди, мілісекунди і мікросекунди:
# Якщо якийсь параметр не заданий, то він дорівнює 0 за замовчуванням.
from datetime import timedelta
delta = timedelta(
    days=50,
    seconds=27,
    microseconds=10,
    milliseconds=29000,
    minutes=5,
    hours=8,
    weeks=2
)

# timestamp 
# це кількість секунд, що пройшло з 00 годин 00 хвилин 1 Січня 1970 року в UTC (часовий пояс Гринвіча). Це просто прийнята константа і нічого особливого вона не означає. Просто для зручності колись почали відраховувати час в секундах з цієї миті і це виявилося дуже зручно. Адже порівняти два числа завжди легше і швидше, ніж порівняти складну структуру дат і часів.

now_date = datetime.now()
ts = print(now_date.timestamp())

# Дату в строку
print(now_date.strftime('%A %d %B %Y'))

# Наоборот
s = '04 September 2001'
print(datetime.strptime(s, '%d %B %Y'))

# random
import random

# print(random.randint(1, 100))

# 0 - 1
# print(random.random())

# Функція random.randrange поверне довільне число від 1 до 10 включно. Зазначене під час виклику число 11 не з'явиться при виклику функції.
print(random.randrange(1, 11))

# MIX the objects
fruits = ['apple', 'banana', 'orange']
random.shuffle(fruits)
# print(fruits)

# Take the random elements from list
fruits = ['apple', 'banana', 'orange']
# print(random.choice(fruits))

# Choose some amount of elements
fruits = ['apple', 'banana', 'orange']
# print(random.choices(fruits, k=4))

# Выбрать элементы чтоб не повторялись K не может быть больше длинны списка и тд
fruits = ['apple', 'banana', 'orange']
# print(random.sample(fruits, k=2))


import collections

Person = collections.namedtuple('Person', ['name', 'last_name', 'age', 'birth_place', 'post_index'])
person = Person('Vadim', 'Chepi', 22, 'Odesa', '00678')

# Обращаемся к ним
# print(person.name)
# print(person.post_index)
# print(person.age)
# print(person[3])

# Считаем к-тво елементов в последовательности
student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]
mark_counts = {}
for mark in student_marks:
    if mark in mark_counts:
        mark_counts[mark] += 1
    else:
        mark_counts[mark] = 1
# print(mark_counts)

# BUT COUNTER
import collections

student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]
mark_counts = collections.Counter(student_marks)
# print(mark_counts)

# COUNTER може вивести елементи за частотою появи:
import collections

student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]
mark_counts = collections.Counter(student_marks)
# print(mark_counts.most_common(1))
# print(mark_counts.most_common(2))

# Ще Counter може відняти кількість елементів одного Counter від другого поелементно:
from collections import Counter

c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
c.subtract(d)  # c - d
# print(c)

# Це спеціальний словник, який створює значення для ключів, яких в словнику не було за запитом. Наприклад, у вас є список слів і ви хочете розбити його на декілька списків, залежно від першої літери слова.
words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
grouped_words = {}

for word in words:
    char = word[0]
    if char not in grouped_words:
        grouped_words[char] = []
    grouped_words[char].append(word)

print(grouped_words)

# BUT
from collections import defaultdict

words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
grouped_words = defaultdict(list)
for word in words:
    char = word[0]
    grouped_words[char].append(word)

# Списки у Python реалізовані таким чином, що вибір елемента за індексом відбувається за константний час (дуже швидко) і додавання/видалення елементу в кінець списку теж відбувається дуже швидко. Але ось додавання елементу в будь-яке інше місце в списку змушує Python перерахувати індекси усіх елементів списку до кінця. Для великих списків це може бути дуже невигідно. Щоб швидко додавати елементи на початок списку, в Python в пакеті collections є така колекція як deque:
from collections import deque

d = deque()
d.append('last')
d.appendleft('first')
d.insert(1, 'middle')
print(d)  # deque(['first', 'middle', 'last'])

print(d.pop())  # 'last'
print(d.popleft())  # 'first'
print(d)  # deque(['middle'])

# Ще однією особливістю deque є можливість обмежити розмір deque:
# Як видно з прикладу, нові елементи витісняють старіші, але розмір залишається незмінним.
# В іншому deque веде себе точно як список Python.

from collections import deque

d = deque(maxlen=5)
for i in range(10):
    d.append(i)

print(d)

# comprehensions — це синтаксична конструкція Python, створена спеціально, щоб зменшити кількість коду, коли потрібно для кожної ітерації циклу for додати один елемент у нову колекцію.

# Щоб записати до списку числа від 1 до 5 за допомогою comprehensions:

numbers = [i for i in range(1, 5 + 1)]
# print(numbers)

# for sets
numbers = [1, 4, 1, 3, 2, 5, 2, 6]
sq = {i ** 2 for i in numbers}
# print(sq)

# Для словників синтаксис comprehension трохи відрізняється, оскільки потрібно явно вказати ключ та значення:
# В цьому прикладі ми записали в словник sq числа від 1 до 5 у якості ключів, а їх квадрати як значення. Основна відмінність за синтаксисом — це двокрапка між ключем і значенням в лівій частині виразу всередині дужок.
numbers = [1, 4, 1, 3, 2, 5, 2, 6]
sq = {i: i ** 2 for i in numbers}
print(sq)



