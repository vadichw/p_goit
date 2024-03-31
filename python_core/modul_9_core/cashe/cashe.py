# def outer(x):
#     def inner(y):
#         print(f'{x} + {y} = {x + y}')
#     return inner

def get_cache():
    cache = {}

    def inner(n):
        print(cache)
        if n not in cache:
            cache[n] = sum([i for i in range(1, n + 1)])
            print(f'Hard work {n}')
            return cache[n]
        else:
            print(f'Easy work {n}')
            return cache[n]

    return inner


def main():
    # adder_two = outer(2)
    # adder_two(3)
    calc = get_cache()
    print(calc(5))
    print(calc(10))
    print(calc(5))
    








if __name__ == '__main__':
    main()