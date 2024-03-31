# Інкапсуляція

# class A:
#     def _protected(self):
#         print('Protected')

#     def __secret(self):
#         print("Secret")

# a = A()
# a._protected()
# a._A__secret()

# class Animal:
#     def __init__(self, nickname, age, weight) -> None:

#         self.__nickname = None
#         self.__age = None
#         self.__weight = None

#         self.name = nickname
#         self.age = age
#         self.weight = weight

#     # name
#     @property  
#     def name(self):
#         return self.__nickname

#     @name.setter
#     def name(self, nickname):
#         if len(nickname) > 0:
#             self.__nickname = nickname
#         else:
#             raise ValueError("Give a name for Animal")

#     # age
#     @property
#     def age(self):
#         return self.__age

#     @age.setter
#     def age(self, age):
#         if age in list(range(0, 50)):
#             self.__age = age
#         else:
#             raise ValueError("It`s too big or small age for Animal")

#     weight
#     @property
#     def weight(self):
#         return self.__weight

#     @weight.setter
#     def weight(self, weight):
#         if weight > 0 :
#             self.__weight = weight
#         else:
#             raise ValueError("Imposible weight for animal")

# animal = Animal('Simon', 4, 0) # in this way it works
# print(animal.name, animal.age, animal.weight)


############ Різниця між classmethod and staticmethod #############################

# class Decorator:

#     def doubler(self, x):
#         print("Множення на 2")
#         return x * 2

#     @classmethod
#     def triples(cls, x):
#         print('Множення на 3')
#         return x * 3

#     @staticmethod
#     def quad(x):
#         print('Множення на 4')
#         return x * 4


# decorator = Decorator()
# print("Виклик через экземпляр классу")
# print(decorator.doubler(10))
# print(decorator.triples(10))
# print(decorator.quad(10))

# print("Виклик через класс")
# print(Decorator.quad(3))


######################## Декоратори класів ##################################

# def method_decorator(func):
#     def wrapper(self, *args):
#         print("The method decorator run")
#         result = func(self, args)
#         print("Decorator end")
#         return result
#     return wrapper


# def class_decorator(cls):
#    print("The class method decorator run")
#    new_cls = cls
#    new_cls.value = 45
#    return new_cls


# @class_decorator
# class TestClass:
#     name = "TestClass"

#     @method_decorator
#     def info(self, user):
#         return f"Hello, {user}, this is {self.name}"


# t = TestClass()
# print(t.info("Vadim"))
# print(t.value)


#################### Сховище з паролями ######################

# class KeyStore:
#     def __init__(self, name, password) -> None:
#         self.__password = None
#         self.__name = None

#         self._secret = None

#         self.name = name
#         self.password = password


#     @property
#     def name(self):
#         return self.__name

#     @name.setter
#     def name(self, name):
#         if len(name) > 0:
#             self.__name = name
#         else:
#             raise ValueError("Enter name")


#     @property
#     def password(self):
#         return "Password don`t show"

#     @password.setter
#     def password(self, value):
#         if self.__password is None:
#             self.__password = value
#         else:
#             if self.is_validete():
#                 self.__password = value


#     @property        
#     def secter(self):
#         return self._secret

#     @secter.setter
#     def secret(self, value):
#         if self.is_validete():
#             self._secret = value


#     def is_validete(self):
#         p = input("Password: ")
#         if self.__password == p:
#             print("Ok")
#             return True
#         else:
#             print("Wrong password")
#             return False

# k_store = KeyStore('Vadim', '123456')
# print("Read password")
# print(k_store.password)

# print("set new password")
# k_store.password = "45678"

# print("Secret")
# k_store.secret = "Test"
# print(k_store.secret)


################################## TASK #########################################

# class Adder:
#     def __add__(self, other):
#         raise NotImplemented
#
#
# class ListAdder(Adder):
#     def __init__(self, value):
#         self.value = value
#
#     def __add__(self, other):
#         return self.value + other.value
#
#
# class DictAdder(Adder):
#     def __init__(self, value):
#         self.value = value
#
#     def __add__(self, other):
#         return {**self.value, **other.value}
#
#
# la1 = ListAdder([1, 2,])
# la2 = ListAdder([3, 4])
# print(la1 + la2)
#
# di1 = DictAdder({"Vadim": 22, "Vika": 21})
# di2 = DictAdder({"Anna": 26, "Vlad": 28})
# print(di1 + di2)

######################## Логічні оператори #######################################

# class Car:
#     def __init__(self, year, mark, model, color, price):
#         self.year = year
#         self.mark = mark
#         self.model = model
#         self.color = color
#         self.price = price
#
#     def __eq__(self, other):
#         return self.price == other.price
#
#     def __ne__(self, other):
#         return self.price != other.price
#
#     def __lt__(self, other):
#         return self.price < other.price
#
#     def __gt__(self, other):
#         return self.price > other.price
#
#     def __le__(self, other):
#         return self.price <= other.price
#
#     def __ge__(self, other):
#         return self.price >= other.price
#
#
#
#
# car_a = Car(2017, "BMW", "MD", "black", 5000)
# car_b = Car(2001, "Audi", "LS", "white", 15000)
#
# print(car_a == car_b)




################# task #####################

# class Animal:
#     def __init__(self, nickname, age, weight) -> None:
#
#         self.__nickname = None
#         self.__age = None
#         self.__weight = None
#
#         self.name = nickname
#         self.age = age
#         self.weight = weight
#
#     # name
#     @property
#     def name(self):
#         return self.__nickname
#
#     @name.setter
#     def name(self, nickname):
#         if len(nickname) > 0:
#             self.__nickname = nickname
#         else:
#             raise ValueError("Give a name for Animal")
#
#     # age
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age):
#         self.__age = age
#
#     #weight
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, weight):
#         if weight > 0 :
#             self.__weight = weight
#         else:
#             raise ValueError("Imposible weight for animal")
#
# # animal = Animal('Simon', 4, 20) # in this way it works
# # print(animal.name, animal.age, animal.weight)
#
# class Turtle(Animal):
#     def __init__(self, nickname, age, weight):
#         super().__init__(nickname, age, weight)
#
#     @Animal.age.setter
#     def age(self, age):
#         if age in list(range(0, 150)):
#             Animal.age.fset(self, age)
#         else:
#             raise ValueError("Error age")
#
# turtle = Turtle("Donatelo", 120, 90)
# print(turtle.name, turtle.age, turtle.weight)


################# Simple Read ##########################

from time import time

# WRONG
# def read_file(filename):
#     text_file = open(filename, 'r')
#     lines = text_file.readlines()
#     text_file.close()
#     return lines
#
# start = time()
# data = read_file('new.txt')
# print(time()- start)


def read_file_yield(filename):
    text_file = open(filename, 'r')
    while True:
        lines = text_file.readline()
        if not lines:
            text_file.close()
            break
        yield lines

start = time()
data = read_file_yield('new.txt')
print(time()- start)




