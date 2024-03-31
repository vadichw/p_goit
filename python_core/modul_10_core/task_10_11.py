from collections import UserString


class NumberString(UserString):
   def number_count(self):
        count = sum(char.isdigit() for char in self.data)
        return count
   
my_string = NumberString("Hello12345World")
count_of_numbers = my_string.number_count()
print(f"Number of digits in the string: {count_of_numbers}")