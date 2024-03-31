from collections  import namedtuple

Person = namedtuple('Person', ['name', 'age', 'city'])
person_1 = Person('Vadim', 23, 'Odesa')
person_2 = Person('Vika', 22, 'Odesa')

print(f"Name: {person_1.name}, {person_1.age}, City: {person_1.city}")
