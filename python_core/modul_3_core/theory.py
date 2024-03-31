#def print_max(a, b):
    #if a > b:
        #print(a, "max")
    #elif a == b:
        #print(a, "дорівнює", b)
    #else:
        #print(b, "max")
#a = 5
#b = 6
#print_max(a, b)
# OR
#print_max(5, 6)

# ОБЛАСТЬ ВИДИМОСТІ ЗМІННОЇ 
x = 50
def fun():
    x = 2
    print("change local value x on", x)
fun()
print("x як і раніше", x)

# GLOBAL
#у = 10
#def f():
    #global y
    #print("y =", y)
    #y = 5
    #print("Змінили глобальне значення у на", y)
#f()
#print("Значення у дорівнює", y)

# LAMBDA

#print((lambda x, y: x + y)(6, 8))

# REKURCIA

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1) # Типа 5 * (5 - 1) = 5 * 4
print(factorial(5))

## FIBONACHI

#def fibonachi(n):
    #if n in (1, 2):
        #return 1
    #return fibonachi( n - 1) + fibonachi(n - 2)
    
#print(fibonachi(10))

def fibonachi_1(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a
print(fibonachi_1(10))

# IMPORT 
from math import pi, sin
sin_pi = sin(pi)
print(sin_pi)

# RANDOM
import random
for item in range(5):
    print(random.randint(1, 10))


import string
str = "hello, my lord"
print(str)
print(string.capwords(str))

