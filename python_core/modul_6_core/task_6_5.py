# 60b90c1c13067a15887e1ae1,Tayson,3
# 60b90c2413067a15887e1ae2,Vika,1
# 60b90c2e13067a15887e1ae3,Barsik,2
# 60b90c3b13067a15887e1ae4,Simon,12
# 60b90c4613067a15887e1ae5,Tessi,5
from pprint import pprint
def get_cats_info(path):
    list = []
    with open(path, 'r') as file:
        for line in file:
            elements = line.strip().split(',')

            id = elements[0]
            name = elements[1]
            age = elements[2]

            info = {'id': id, 'name': name, 'age': age,}
            list.append(info)

        return list
pprint(get_cats_info('test.txt'))