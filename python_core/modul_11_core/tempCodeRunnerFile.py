class Animal:
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
    
#     # weight
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