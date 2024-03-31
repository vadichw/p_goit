def is_valid_pin(pin_codes):
    if not pin_codes:
        return False

    unique_pin = set(pin_codes)

    if len(unique_pin) != len(pin_codes):
        return False
    
    for pin_code in unique_pin:
        if len(pin_code) != 4 or not pin_code.isdigit(): # isdigit - проверяет есть ли в строке числа
            return False
    return True


pin = is_valid_pin(["1111","222"])
print(pin)
