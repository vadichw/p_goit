DEFAULT_DISCOUNT = 0.05


def get_discount_price_customer(price, customer):
    dis = customer.get("discount", DEFAULT_DISCOUNT )
    dis_price = price * (1 - dis)
    return dis_price