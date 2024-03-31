class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Owner:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.adress = address  

    def info(self):
        return {'name': self.name, 'age': self.age, 'adress': self.adress}


class Dog(Animal):
    def __init__(self, nickname, weight, breed, owner ):
        super().__init__(nickname, weight)
        self.breed = breed
        self.owner = owner

    def say(self):
        return "Woof"

    def who_is_owner(self):
        return self.owner.info()

owner = Owner('John', 30, '123 Main St')
dog = Dog('Buddy', 2, 'black', owner)

print(dog.owner.info())