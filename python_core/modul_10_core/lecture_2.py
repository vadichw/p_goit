# Качина типізація

# class Animal:
#     def __init__(self, nickname: str, age: int):
        
#         self.nickname = nickname
#         self.age = age

#     def sound(self) -> str:  
#         pass


# class Cat:
#     def __init__(self, nickname: str, age: int,) -> None:
        
#         self.nickname = nickname
#         self.age = age

#     def sound(self) -> str:
#         return f"{self.nickname}, his age is {self.age} and he say:'meow'"


# class Dog:
#     def __init__(self, nickname: str, age: int,) -> None:
        
#         self.nickname = nickname
#         self.age = age
        
#     def sound(self) -> str:
#         return f"{self.nickname}, his age is {self.age} and he say:'wouf'"


# def pet_say(pet: Animal):
#     print(pet.sound())

# animal = Animal('Chupakabra', 50)
# cat = Cat('Simon', 5)
# dog = Dog('Jack', 10)

# for pet in (animal, cat, dog):
#     pet_say(pet)

################################

# class Duck:
#     def swim_quack(self):
#         print("I am duck and I can swim")


# class RobotBird:
#     def swim_quack(self):
#         print("I am robot bird")


# class Fish:
#     def swim(self):
#         print("I can swim")


# def duck_testing(animal):
#     animal.swim_quack()


# duck_testing(Duck())
# duck_testing(RobotBird())
# duck_testing(Fish())


##################################
# Store 
#price, name, amount 
###################################
# class ProductInStore:
#     def __init__(self, price: float, name: str) -> None:
#          self.price = price
#          self.name = name
         
#     def set_price(self, price):
#         self.price = price
        
#     def set_name(self, name):
#         self.name = name
    
#     def set_stock(self, qty):
#         self.qty_in_stock = qty # the amount of goods
    
# model = ProductInStore(300, 'Lego Ship')
# model.set_stock(10)

# print(model.name, model.price, model.qty_in_stock)


###########################################
# 185 - числове значення
# 1, 2, 5, 10, 25, 50 - номінали копійок 

class Coins:
    def __init__(self, total_sum) -> None:
        self._coins = (1, 2, 5, 10, 25, 50) # _coins означает шо это значение лучше не менять
        self.total_sum = total_sum
        
        
    def change(self):
        result = {}
        item = len(self._coins) - 1 # item : 5 = 6 - 1
        while item >= 0:
            coin = self._coins[item] # coin : 50 
            num_of_coin = self.total_sum // coin # 185 // 50 = 3 ......35//25=1
            result[coin] = num_of_coin # add to dict result[50] = 3.....1
            self.total_sum -= coin * num_of_coin # self.total_sum 185 - (50*3).......35 - ()
            item -= 1 # 5 - 1 = 4
        return result
    
test = Coins(185)
print(test.change())
    
    
    
    
    