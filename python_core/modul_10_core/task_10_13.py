class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Cat(Animal):
    def say(self):
        return "Meow"


class CatDog:
    def __init__(self, nickname, weight):
        self.cat = Cat(nickname, weight)
        self.nickname = nickname
        self.weight = weight

    def say(self):
        return self.cat.say()

    def change_weight(self, weight):
        self.cat.change_weight(weight)

cat_dog = CatDog("Fluffy", 10)
cat_dog.change_weight(5)