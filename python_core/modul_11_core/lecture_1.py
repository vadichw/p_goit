# сначала __new__, потом __init__

# class Foo:
#     def __init__(self, value) -> None:
#         print("Constructor Foo")
#         self.value = value

#     def __new__(cls, *args, **kwargs):
#         print("Method class Foo")
#         instance = super(Foo, cls).__new__(cls)
#         return instance
    

# class Baz(Foo):
#     def __init__(self, value) -> None:
#         super(Baz, self).__init__(value)

# baz = Baz(10)
# foo = Baz(20)

# print(baz.value, foo.value)

#############Singleton##################
# class Singleton:
#     instance = None

#     def __new__(cls, *args, **kwargs):
#         if cls.instance is None:
#             cls.instance = super(Singleton, cls).__new__(cls)
#         return cls.instance
    
#     def __init__(self, value) -> None:
#         self.value = value

# foo = Singleton(10)
# baz = Singleton(20)
# bar = Singleton(30)

# print(foo.value, baz.value, baz.value)

########################################################
# __str__, __repr__

# class Car:
#     store_name = 'Store'

#     def __init__(self, year, mark, model, color) -> None:
#         self.year = year
#         self.mark = mark
#         self.model = model
#         self.color = color

#     def __str__(self) -> None:
#         return f"{self.store_name}: {self.mark}, {self.model}, {self.year}, {self.color}"
    
#     def __repr__(self) -> None:
#         return f"Car : {self.mark}, {self.model}"

# car = Car(2019, 'BMW', 'V2000', 'black')
# print(car)
# print(repr(car))

###########################################################
#getitem, setitem

# from collections import UserList

# class PositiveNumber(UserList):
#     def __init__(self, data = []):
#         super(PositiveNumber, self).__init__()
#         self.data = [el for el in list(filter(lambda x: x > 0, data))]
    
#     def __getitem__(self, index): # Буде спрацювувати завжди коли ми звертаємося по індексу
#         if index is None:
#             return self.data
#         return self.data[index]
    
#     def __setitem__(self, key, value):
#         if value > 0 and key < len(self.data):
#             self.data[key] = value

#     def append(self, item) -> None:
#         if item > 0:
#             super().append(item)

# nums = PositiveNumber([2, -4, 5])
# print(nums)
# print(nums[None])
# nums[1] = -2
# nums[1] = 3
# nums.append(-11)
# print(nums[None])

#### call ###############
# Функтор 
#  Тепер об'єкти цього класу можна викликати як функцію, передаючи їм аргументи. Ці виклики будуть викликати метод __call__ в об'єктів класу

# class Counter:
#     def __init__(self, init_steps) -> None:
#         self.init_steps = init_steps
    
#     def __call__(self, *args, **kwargs):
#         inc, = args # args -> tuple(100, ...)
#         self.init_steps += inc
        
# count_step = Counter(100)
# count_step(50)
# count_step(25)
# print(count_step.init_steps)


# Менеджери контексту 

# Custom with....as....

# class FileWriter:
#     def __init__(self, filename) -> None:
#         self.file = None
#         self.filename = filename
#         self.opened = False # flags
        
#     def __enter__(self):
#         self.file = open(self.filename, 'w')
#         self.opened = True
#         return self.file
    
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if self.opened:
#             self.file.close()
#         self.opened = False
        
# if __name__ == '__main__':
#     with FileWriter('new_file.txt') as f:
#         f.write('Hi\n')
#         f.write('Hello\n')

# from datetime import datetime
# from time import sleep


# class FileReader:
#     def __init__(self, filename) -> None:
#         self.file = None
#         self.filename = filename
#         self.opened = False # flags
#         self.log = ''
#         self.timestamp = None
        
#     def __enter__(self):
#         self.file = open(self.filename, 'r')
#         self.opened = True
#         self.timestamp = datetime.now().timestamp()
#         msg = '{:<20}|{:^15}| open\n'.format(self.timestamp, self.filename)
#         self.log += msg
#         return self.file

    
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if self.opened:
#             self.file.close()
#             timestamp = datetime.now().timestamp()
#             diff = timestamp - self.timestamp
#             msg = '{:<20}|{:^15}| close {:>15}\n'.format(timestamp, self.filename, round(diff, 3))
#             self.log += msg
#         self.opened = False
        
# reader = FileReader('new_file.txt')

# with reader as file:
#     sleep(1)
#     print(file.read())

# print(reader.log)

################ contextmanager ##########################
# from contextlib import contextmanager

# @contextmanager
# def manager_resource(*args, **kwargs):
#     file_handler = open(*args, **kwargs)
#     try:
#         yield file_handler
#     finally:
#         file_handler.close()
        
# with manager_resource('new_file.txt', 'r') as file:
#     print(file.read())

##### iter ###########

# from random import randint
#
# class RandIterator:
#     def __init__(self, start, end, quantity) -> None:
#         self.start = start
#         self.end = end
#         self.quantity = quantity # Необхідна кількість
#         self.count = 0 # Лічильник
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.count += 1
#         if self.count > self.quantity:
#             raise StopIteration
#         return randint(self.start, self.end)
#
# my_random_list = RandIterator(1, 20, 5)
#
# for item in my_random_list:
#     print(item, end = ' ')


