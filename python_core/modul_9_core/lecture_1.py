# Записали функцию в переменную

# def mul(a, b):
#     return a*b

# f = mul 
# result = f(10, 10)
# print(result)


# Передали функцию как аргумент 

# def mul(a,b):
#     return a*b

# def add(a,b):
#     return a+b

# def ops(a,b, func):
#     return func(a,b)

# result = ops(3,5,add)
# print(result)

# Функция может быть возвращенна как результат

# def mul(a,b):
#     return a*b

# def add(a,b):
#     return a+b

# def ops(operator: str):
#     if operator == '*':
#         return mul
#     elif operator == '+':
#         return add
#     else:
#         raise ValueError('Operator is not support')
    
# f_mul = ops('*')
# print(f_mul)

# result = f_mul(3, 5)
# print(result)

#######################################
# Замыкание
# def outer():
#     msg = 'Hi'
    
#     def inner():
#         print(msg)
        
#     return inner

# f = outer()
# f()

# def greeting(name):
    
#     def msg(m):
        
#         return f"{name}, {m}"
    
#     return msg

# msg = greeting('Vadim')
# print(msg('learn Python'))
#########
# def taxer(base_tax):
#     def calculate(money):
#         nonlocal base_tax
#         if money >= 10000:
#             base_tax = 1.5 * base_tax
#         return money - base_tax * money
#     return calculate

# ukr = taxer(0.1)
# swd = taxer(0.5)

# money_ukr = ukr(5000)
# money_swd = swd(10000)

# print(money_ukr)
# print(money_swd)

# def factorial_with_cashe():
#     cashe = {}
    
#     def calc(n):
#         if n < 0:
#             raise ValueError("Number is less 0")
        
#         result = 1
#         for value in range(1, n + 1):
#             if value in cashe:
#                 result = cashe[value]
#                 print(f"{value} in cashe")
#             else:
#                 result =  value * cashe.get(value - 1, 1)
#                 cashe[value] = result
#                 print(f"{value} NOT in cashe")
#         return result
#     return calc

# factorial = factorial_with_cashe()
# f3 = factorial(3)
# print(f3)
# f5 = factorial(5)
# print(f5)



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
# print(f"{f3(3)}")
# f5 = factorial(5)
# print(f"{f5(5)}")

# КАРУВАНННЯ

# def greeting(name):
    
#     def message(msg):
#         return f"{name}, {msg}"
    
#     return message


# msg_for_vadim = greeting('Vadim')
# print(msg_for_vadim('learn Python'))


# DECARATION

#def greeting(val):
#     print(f"My name is {val}")
    
# def greeting_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Hello")
#         result = func(*args, **kwargs)
#         print("Goodbye")
#         return result
#     return wrapper

# greeting('Vadim')
# change_greeting = greeting_decorator(greeting)
# print(change_greeting('Vadim'))



# def decorator_name(func):
#      def wrapper(name, surname):
#          result = func(name, surname)
#          print("Goodbye")
#          return result
#      return wrapper
 
# def prefix(func):
#     def wrapper(name, surname):
#         print("Prefix")
#         name = f"Mr {name}"
#         result = func(name, surname)
#         return result
#     return wrapper
 
# @decorator_name
# @prefix
# def full_name(name, surname):
#     print(f"Hello, {name} {surname}")
    

# full_name("Vadim", "Chepik")



