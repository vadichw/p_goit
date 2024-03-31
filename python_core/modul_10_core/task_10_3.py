class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, changed_weight):
        self.weight = changed_weight


animal = Animal("Simon", 10)
animal.change_weight(12)
