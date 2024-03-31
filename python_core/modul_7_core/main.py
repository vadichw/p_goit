# from my_package import foo
# print(foo.foo("vadim"))

from my_package.foo import foo
from my_package.baz.operation import sum, mul
from my_package.bar.info import log

# from my_package import foo, sum, mul, log

# import my_package
# print(my_package.foo('lord'))


if __name__ == "__main__":
    print(foo('lord'))
    print(sum(5,5))
    print(mul(10,5))
    log('Vadim')
    print()
