import pickle
import json
from pprint import pprint
import csv
#
# d = {'some key': 123}
#
# with open('data.bin', 'wb') as file:
#     pickle.dump(d, file)
#
# with open('data.bin', 'rb') as file:
#     db = pickle.load(file)
#
# p = pickle.dumps(d)
# print(p)
# print(db)


# FILENAME = 'users.dat'
#
# users = [
#     ['Jack', 22, True, ],
#     ['Vadim', 23, False]
# ]
#
# with open(FILENAME, 'wb') as file:
#     pickle.dump(users, file)
#
# with open(FILENAME, 'rb') as file:
#     users_from_file = pickle.load(file)
#     for user in users_from_file:
#         print(f'Name {user[0]}\t Age: {user[1]}\t Status: {user[2]}\t')

# class A:
#     x = 'some'
#
#     def __init__(self):
#         print("New A!")
#         self.y = "Another value"
#
#
# a = A()
# s = pickle.dumps(a)
# s_class = pickle.dumps(A)
# restored_a = pickle.loads(s)
# restore_A = pickle.loads(s_class)
#
# print(a.x, a.y)
# print(restored_a.x, restored_a.y)


# d = {'a': 1}
# l = [1, 2]
# t = (3, 4)
# s = 'it string'
# b = True
# st = {1, 3, 5, 'test'}
#
# obj = {'dict': d, 'list': l, 'tuple': t, 'string': s, 'boolean': b}
# print(json.dumps(b))
#
# with open('storage.json', 'w') as file:
#     json.dump(obj, file)
#
# with open('storage.json', 'r') as file:
#     storage = json.load(file)
#
# print(storage)
# print(storage.get('dict'))
# print(storage.get('tuple'))
#
# data = {
#     'developer': {
#         'name': 'Vadim',
#         'species': 'Programist'
#     }
# }
#
# with open('data_user.json', 'w') as file:
#     json.dump(data, file)
#
# with open('data_user.json', 'r') as file:
#     un = json.load(file)
#
# pprint(un)


# with open('name.csv', 'w', newline='\n') as file:
#     fields_name = ['firstname', 'lastname']
#     writer = csv.DictWriter(file, fieldnames=fields_name)
#     writer.writeheader()
#     writer.writerow({'firstname': 'Vadim', 'lastname': 'Chepik'})
#     writer.writerow({'firstname': 'Frodo', 'lastname': 'Begins'})
#
# with open('name.csv', 'r') as file:
#     print(file.read())

# table #

# name = 'tables.csv'
#
# with open(name, 'w') as file:
#     writer = csv.writer(file)
#     for i in range(1,11):
#         writer.writerow([i, i**2, i**3])



