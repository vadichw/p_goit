class User:
    def __init__(self, name, age):
        self.__private_name = None
        self.__private_age = None

        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__private_name

    @name.setter
    def name(self, value: str):
        if value.isalpha():
            self.__private_name = value
        else:
            raise Exception("Wrong name")

    @property
    def age(self):
        return self.__private_age

    @age.setter
    def age(self, value):
        if int(value) >= 18:
            self.__private_age = int(value)
        else:
            raise Exception("Wrong age")


user_1 = User("Vadim", 22)
print(user_1.name, user_1.age)
