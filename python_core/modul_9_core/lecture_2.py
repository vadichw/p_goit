# Зробити декоратор який повертає кортеж з результатом обчислення факторіалу та часом виконачання

# from time import time, sleep

# def time_counter(func):
    
#     def interval(*args, **kwargs):
#         start = time()
#         result_t = func(*args, **kwargs)
#         passed = time() - start
#         return passed, result_t
    
#     return interval


# @time_counter
# def factorial(n, cashe={}):
#         if n < 0:
#             raise ValueError("Number is less 0")
    
#         def calc(n):
#             result = 1
#             for value in range(1, n + 1):
#                 if value in cashe:
#                     result = cashe[value]
#                     print(f"{value} in cashe")
#                 else:
#                     result =  value * cashe.get(value - 1, 1)
#                     cashe[value] = result
#                     print(f"{value} NOT in cashe")
                    
#             return result

#         return calc

# f3 = factorial(3)
# print(f"{f3}")
# f5 = factorial(5)
# print(f"{f5}")


# Генератор шо вернет рандомное число между мин и макс в бесконечном цикле

#from random import randint, seed

# def simple_gen():
#     yield 'First'
#     yield 'Second'

# for r in simple_gen():
#     print(r)

# gen = simple_gen()
# print(gen)

# r = next(gen)
# print(r)

# r = next(gen)
# print(r)

# r = next(gen) # тут будет ошибка 
# print(r)

# Свой генератор range

# def my_range(limit):
#     value = 0
#     while value < limit:
#         yield value
#         value = value + 1

# gen = my_range(5)

# while True:
#     try:
#         r = next(gen)
#         print(r)
#     except StopIteration:
#         break

#####
# sq_gen = (i**2 for i in range(10))
# print(sq_gen)

# for i in sq_gen:
#     print(i, ' ', end='')



# LAMBDA

# def sq_normal(x):
#     return x ** 2

# sq = lambda x: x **2 # НИЗЯ ЛАМБДУ ПРИСВАИТЬ КАК ЗНАЧЕНИЕ ПЕРЕМЕННОЙ


# print(sq_normal(5))
# print(sq(5))



# map

names = ['vadim', 'vika', 'vlad',]

def normalize(name):
    return name.title()

# 1
new_names = []
# for name in names:
#     new_names.append(name.title())
# print(new_names)

# 2
# new_names = map(normalize, names)
# print(list(new_names))

# 3
# new_names = map(str.title, names)
# print(list(new_names))

# 4
# new_name = list(map(lambda name: name.title(), names))
# print(new_name)

# # 5
# new_name = [name.title() for name in names]
# print(new_name)


# FILTER

# payment = [100, -3, 150, -15]

# def is_negative_number(num) -> bool:
#     if num < 0:
#         return True
#     return False

# p_values = filter(is_negative_number, payment)
# print(list(p_values))

# p1_values = filter(lambda num: num > 0, payment)
# print(list(p1_values))

# Maps and filters

nums = [i for i in range(1,10)]
print(nums)

sq = map(lambda x: x**2, nums)

result = filter(lambda x: not bool(x % 2), sq)
print(list(result))
result1 = filter(lambda x: bool(x % 2), sq)
print(list(result1))