# class Animal:
#     def __init__(self, name: str, age: int):  # конструктор классу, нічого не повертає
#         # Ініціалізація атрибутів
#         self.name = name  # поля екземплярів класу
#         self.age = age

#     def get_info(self) -> str:  # Метод
#         return f"It`s animal {self.name} and his age is {self.age}"

# animal_obj = Animal('Seman', 3)  #Екземпляр классу
# print(animal_obj.get_info())
# animal_obj.age = 10
# print(animal_obj.get_info())
# animal_obj.name = 'Jack'
# print(animal_obj.get_info())

########################################################


# # НАСЛЕДОВАНИЕ
# class Animal:
#     def __init__(self, name: str, age: int):  # конструктор классу, нічого не повертає
#         # Ініціалізація атрибутів
#         self.name = name  # поля екземплярів класу
#         self.age = age

#     def get_info(self) -> str:  # Метод
#         return f"It`s animal {self.name} and his age is {self.age}"


# class Cat(Animal):
#     def __init__(self, name: str, age: int, owner) -> None:
#         super().__init__(name, age)
#         self.owner = owner
        
#     def sound(self) -> str:
#         return f"Cat {self.name}, his age is {self.age} and he say: 'meow' "
    

# cat = Cat('Simon', 10, 'Vadim')
# print(cat.name)
# print(cat.get_info())
# print(cat.sound())


# class Car:
#     brand = 'Mersedez'
    
# ex_1 = Car()
# ex_2 = Car()

# Car.brand = 'Tesla'
# print(ex_1.brand, ex_2.brand)


# class Car():
#     def __init__(self):
#         self.brand = 'Mersedez'

# ex_1 = Car()
# ex_2 = Car()

# ex_1.brand = 'BMW'

# print(ex_1.brand, ex_2.brand)



### ПОЛИМОРФИЗ ###

# class Animal:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age

#     def get_info(self) -> str:  # Метод
#         return f"It`s animal {self.name} and his age is {self.age}"


# class Cat(Animal):
#     def __init__(self, name: str, age: int, owner) -> None:
#         super().__init__(name, age)
#         self.owner = owner
        
#     def sound(self) -> str:
#         return f"Cat {self.name}, his age is {self.age} and he say:'meow'"
    
#     def get_info(self) -> str: 
#         return f"Cat {self.name} and his age is {self.age}"


# class Dog(Animal):
#     def __init__(self, name: str, age: int, owner) -> None:
#         super().__init__(name, age)
#         self.owner = owner
        
#     def sound(self) -> str:
#         return f"Cat {self.name}, his age is {self.age} and he say:'gav-gav'"
    
#     def get_info(self) -> str:
#         return f"Dog {self.name} and his age is {self.age}"
    
# cat = Cat('Jack', 10, 'Vadim')
# dog = Dog('Nike', 5, 'Vika')

# print(isinstance(dog, Animal)) # True
# print(isinstance(dog, Cat)) # False
# print(isinstance(dog, Dog)) # True

# print(dog.get_info())
# print(cat.get_info())

# print(type(dog) is Animal) # False
# print(type(dog) is Dog) # True

# for el in (cat, dog):
#     if type(el) is Dog:
#         print(f"{el.sound()} {el.get_info()}")
        



# class Animal:
#     def __init__(self, nickname: str, age: int):
#         self.nickname = nickname
#         self.age = age

#     def get_info(self) -> str:  # Метод
#         return f"It`s animal {self.nickname} and his age is {self.age}"
    
    
# class Owner:
#     def __init__(self, name, phone) -> None:
#         self.name = name
#         self.phone = phone
        
#     def info(self) -> str:
#         return f"{self.name} : {self.phone}"
    

# class Cat(Animal):
#     def __init__(self, nickname: str, age: int, name, phone) -> None:
#         super().__init__(nickname, age)
#         self.owner = Owner(name, phone)
        
#     def sound(self) -> str:
#         return f"Cat {self.nickname}, his age is {self.age} and he say:'meow'"
    
#     def get_info(self) -> str: 
#         return f"Cat {self.nickname} and his age is {self.age}"
    
# cat = Cat('Semen', 3, 'Vadim', '123456')
# print(cat.owner.info())


############### Агрегация ##############
# class Animal:
#     def __init__(self, nickname: str, age: int):
#         self.nickname = nickname
#         self.age = age

#     def get_info(self) -> str:
#         return f"It`s animal {self.nickname} and his age is {self.age}"

# class Owner:
#     def __init__(self, name, phone) -> None:
#         self.name = name
#         self.phone = phone
        
#     def info(self) -> str:
#         return f"{self.name} : {self.phone}"


# class Cat(Animal):
#     def __init__(self, nickname: str, age: int, owner: Owner) -> None:
#         super().__init__(nickname, age)
#         self.owner = owner
        
#     def sound(self) -> str:
#         return f"Cat {self.nickname}, his age is {self.age} and he say:'meow'"
    
#     def get_info(self) -> str: 
#         return f"Cat {self.nickname} and his age is {self.age}"
    
    
# owner = Owner('Vadim', 123456)
# cat = Cat('Jack', 3, owner)
# print(cat.owner.info())



####### Method Resolution Order ###########

# class A:
#     def hi(self):
#         print('A')

# class B(A):
#     #def hi(self):
#         #print('B')
#         pass
        
# class C(A):
#     def hi(self):
#         print('C')
        
# class D(B, C):
#     pass

# d = D()
# d.hi()



# CONTAINERS
#USERLIST
# from collections import UserList
# from random import randint

# class MyList(UserList):
#     _info = 'This is my list'
    
#     def get_positive(self):
#         return list(filter(lambda x: x > 0, self.data))
    
#     def get_negative(self):
#         return list(filter(lambda x: x < 0, self.data))
    
#     def info(self):
#         return self._info
    
# r = []
# for _ in range(0, 20):
#     r.append(randint(-5, 5))
    
# result = MyList(r)

# print(result)
# print(result.get_positive())
# print(result.get_negative())
# print(result.info())


#USERDICT
# from collections import UserDict

# contacts = [{
#     "name": "Allen Raymond",
#     "email": "nulla.ante@vestibul.co.uk",
#     "phone": "(992) 914-3792",
#     "favorite": False,
# }]

# class Customer(UserDict):

#     def get_phone(self):
#         return f"{self.get('name')} : {self.get('phone')}"
    

#     def get_email(self):
#         return f"{self.get('name')} : {self.get('email')}"
    

# customers = [Customer(contact) for contact in contacts]
# #print(customers)
# for customer in customers:
#     print(customer.get_phone())
#     print(customer.get_email())




#USERSTRING

# from collections import UserString

# template = 'Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?'

# # for i, comment in enumerate(template):
# #     print('|{:^5}|{:<15}|'.format(i, comment))


# class Comments(UserString):
#     def get_limit_comment(self, limit=10):
#         return f"{self.data[:limit - 3]}..."
    

# comments = [Comments(comment) for comment in template]
# for i, comment in enumerate(comments):
#     print('|{:^5}|{:<15}|'.format(i, comment.get_limit_comment(35)))



# # EXEPTIONS

# class MyException(Exception):
#     def __init__(self, value) -> None:
#         self.value = value

# def test(value: int):
#     if value < 0:
#         raise MyException(f"{value} < 0")
#     else:
#         return value + 100
    
# try:
#     test(-5)
# except MyException as e:
#     print(e)
    


    


