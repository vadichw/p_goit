# def get_numbers(x):
#     numbers =[]
#     for i in range(x):
#         num = i ** 2
#         if num % 2 == 0:
#             numbers.append(num)
#     print(numbers)

# get_numbers(20)

def get_num(x):
    print([i**2 for i in range(x) if i % 2 == 1])
    print({i: i**2 for i in range(x) if i % 2 == 1})

get_num(20)