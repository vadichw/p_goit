def amount_payment(payment):
    sum = 0
    for num in payment:
        if num > 0:
            sum += num
    return sum

print(amount_payment([1,5,-4.-10]))