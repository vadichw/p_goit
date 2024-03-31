class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight
        
class Cat(Animal):
    def __init__(self, nickname, weight):
        super().__init__(nickname, weight) 
        
    def say(self):
        return 'Meow'
    
cat = Cat('Simon', 10)
print(cat.nickname, cat.weight, cat.say())