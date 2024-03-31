from datetime import  datetime, timedelta, MAXYEAR, MINYEAR

# td = '25.11.2023'
# d = datetime.strptime(td, '%d.%m.%Y')
# print(d.date())

# other = d.replace(month=5, day=11, hour=11)
# print(other)

# str_date = other.strftime('%Y/%d/%m')
# str_date_m = other.strftime('%y/%d/%m')
# print(str_date)
# print(str_date_m)

# d = datetime.now()
# interval = timedelta(days=4)
# finish = d + interval
# print(finish)

# birth_date = datetime(2001, 9, 4)
# today = datetime.now() - birth_date
# print(today)

# d = datetime.now()
# print(d.timestamp())
# # Amount of days from 0001???
# print(d.toordinal())
# # Sun Nov 26 11:30:39 2023
# print(d.ctime())

# print(MINYEAR)
# print(MAXYEAR)


import random

# random.seed() # 0-1
# print(random.random())
# print(random.randint(1,10))

# data = list(range(1,11))
# #print(data)

# random.shuffle(data)
# #print(data)

# print(random.choice(data))
# print(random.sample(data, k=5))

# Яку мінімальну к-сть разів треба підкинути монетку щоб 3чі поспіль випав орел чи решка?

d = {
    1 : "Orel",
    2: "Reshka",
}

count_Orel = 0
count_Reshka = 0
sequence = []

while count_Reshka < 3 and count_Orel < 3:
    trial = random.randint(1,2)

    if trial == 1:
        count_Orel += 1
        count_Reshka = 0
    else:
        count_Orel = 0
        count_Reshka += 1

    sequence.append(d[trial])

print(f"You got {sequence}")

if count_Orel == 3:
    print("Got 3 Orla")
else:
    print("Got 3 Reska")

print(f"Amount attemts {len(sequence)}")



from decimal import Decimal, getcontext, ROUND_HALF_EVEN, ROUND_HALF_UP

# f = 0.2 + 0.1 + 0.3 - 0.5
# print(f)

res_dec = Decimal('0.1') + Decimal('0.2') + Decimal('0.3') - Decimal('0.5')
print(res_dec)

not_presicion = Decimal('1') / Decimal('3')
print(not_presicion)

# prec керує точністю чисел, скількі знаків після коми
getcontext().prec = 6
presicion = Decimal('1') / Decimal('3')
print(presicion)

num = Decimal('1.45')
print(num.quantize(Decimal('1.0'), rounding=ROUND_HALF_EVEN)) # 1.4 Машинное округление 
print(num.quantize(Decimal('1.0'), rounding=ROUND_HALF_UP)) # 1.5 Человеческое 
print(Decimal('3.14159').quantize(Decimal('1.00')))

# compare

# 0 - оба числа равны
# 1 - первое БОЛЬШЕ чем второе
# -1 - первое МЕНЬШЕ чем второе
print(Decimal('1.2').compare(Decimal('1.1'))) # 1
print(Decimal('1.0').compare(Decimal('1.1'))) # -1
print(Decimal('1.0').compare(Decimal('1.0'))) # 0

print(0.1 + 0.2 == 0.3) # False

n = Decimal('0.1') + Decimal('0.2')
v = Decimal('0.3')
print(n.compare(v)) # 0 числа равны

import collections

# Point = collections.namedtuple('Point', ['x', 'y', 'z'])
# p = Point(1,2,3)
# print(p)
# print(p.x)

# Cat = collections.namedtuple('Cat', ['name', 'age', 'owner'])
# cat = Cat('Samen', 12, 'Vadim')
# print(f"It`s {cat.name}")

# Есть список температур. Надо найти то значение которое встречается чаще всего
temperature = [0.5, 1.0, 0.5,-3]
temp_counter = collections.Counter(temperature)
print(temp_counter)
print(temp_counter.most_common(1))

from collections import defaultdict

d_data = defaultdict(list)
d_data[0].append(10)
d_data[0].append(20)
d_data[1].append(5)
d_data['key'].append('value')
print(d_data)

colors = [('yellow', 1),('red', 2)]
colors_default = defaultdict(list)
for k, v in colors:
    colors_default[k].append(v)
print(colors_default)


from collections import deque
l = list(range(1,10))
l_deque = deque(l)
print(l_deque)
l_deque = deque(l,5) # take the from right 
print(l_deque)
l_deque.appendleft(25)
print(l_deque)
print(l_deque.count(7))

