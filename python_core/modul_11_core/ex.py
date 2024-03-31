class KeyStore:
    def __init__(self, name, password) -> None:
        self.__name = None
        self.__password = None

        self.__secret = None

        self.name = name
        self.password = password

    @property
    def name(self):
            return self.__name

    @name.setter
    def name(self, name):
            if len(name) > 0:
                self.__name = name
            else:
                raise ValueError("Enter name")

    @property
    def password(self):
            return "Dont show password"

    @password.setter
    def password(self, value):
            if self.__password is None:
                self.__password = value
            else:
                if self.is_validete():
                    self.__password = value

    def is_validete(self):
            p = input(("Enter password"))
            if self.__password == p:
                print("Okay")
                return True
            else:
                print("Wrong password")
                return False

    @property
    def secret(self):
            return self.__secret

    @secret.setter
    def secret(self, value):
            if self.is_validete():
                self.__secret = value


k_store = KeyStore("Vadim", 12345)
print(k_store.password)






