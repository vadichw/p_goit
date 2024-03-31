def positive_values(list_payment):
    positive = list(filter(lambda x: x > 0, list_payment))
    return positive

print(positive_values([100, -3, 400, 35, -100]))
    
