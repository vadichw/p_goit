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


def get_phone_numbers_for_countries(list_phones):

    country_numbers = {
        "UA": [],
        "JP": [],
        "TW": [],
        "SG": [],
    }
    
    for number in list_phones:
        sanitize_phone = sanitize_phone_number(number)

        if sanitize_phone.startswith("380"):
            country_numbers["UA"].append(sanitize_phone)
            
        elif sanitize_phone.startswith("81"):
            country_numbers["JP"].append(sanitize_phone)
            
        elif sanitize_phone.startswith("65"):
            country_numbers["SG"].append(sanitize_phone)
            
        elif sanitize_phone.startswith("886"):
            country_numbers["TW"].append(sanitize_phone)
            
        else:
            country_numbers["UA"].append(sanitize_phone)
            
    return country_numbers


n = get_phone_numbers_for_countries(([' +380998759405', '(818)765347', '88-67658-976', '657 658976']))
print(n)