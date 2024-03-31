def format_phone_number(func):

    def wrapper(phone):
        sanitized_phone = func(phone)
        
        if len(sanitized_phone) == 12:  # Перевірка на повний міжнародний номер
            return "+" + sanitized_phone
        
        elif len(sanitized_phone) < 12:  # Перевірка на короткий номер
            return "+38" + sanitized_phone
        
        else:
            return sanitized_phone  # Якщо номер не відповідає жодному з умов, повертаємо його як є

    return wrapper
    
                        
@format_phone_number
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
    )
    return new_phone


print(sanitize_phone_number('+(050)1234561'))