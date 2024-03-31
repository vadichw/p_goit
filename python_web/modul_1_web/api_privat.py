# SOLID #
# Single Responsible Principle - один класс - один функционал
# Open closed Principle - класс расширил функционал но не изменил

# class User:
#     def __init__(self, name, password):
#         self.name = name
#         self.password = password
#
#     def login(self, name, password):
#         if name == self.name and self.password == password:
#             return True
#         return False
#
# class Admin(User):
#     def __init__(self, name, password, privilages):
#         super().__init__(name, password)
#         self.privilages = privilages
#
#     def priv(self):
#         return self.privilages

############ S #############
# class ValidPhoneException(Exception):
#     pass
#
#
# class PersonFormatterInfo:
#     def value_of(self):
#         raise NotImplementedError
#
#
# class PersonPhoneNumber(PersonFormatterInfo):
#     def __init__(self, phone: str, operator_code: str):
#         if operator_code not in ('050', '068', '095', '096', '099'):
#             raise ValidPhoneException
#         self.phone = phone
#         self.operator_code = operator_code
#
#     def value_of(self):
#         r