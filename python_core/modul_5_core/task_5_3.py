def sanitize_phone_number(phone):
    new_phone = (phone.strip()
                 .removeprefix("+")
                 .replace("(", "")
                 .replace(")", "")
                 .replace("+", "")
                 .replace("-", "")
                 .replace(" ", "")
                 )
    return new_phone

num = sanitize_phone_number("+ 3(80)-5678-23")
print(num)
    