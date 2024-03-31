def discount_price(discount):
    
    def calculate_discounted_price(price):
        discounted_price = price - (price * discount)
        return discounted_price

    return calculate_discounted_price

# Приклад використання:
cost_15 = discount_price(0.15)
cost_10 = discount_price(0.10)
cost_05 = discount_price(0.05)

price = 100
print(cost_15(price))  # Результат: 85.0 (100 - 15%)
print(cost_10(price))  # Результат: 90.0 (100 - 10%)
print(cost_05(price))  # Результат: 95.0 (100 - 5%)

