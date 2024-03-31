from functools import reduce


def amount_payment(payment):
    suma = reduce(lambda x, y: x + y if y > 0 else x, payment)
    return suma

print(amount_payment([1, -3, 4]))