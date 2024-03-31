from random import randint

def get_random_password():
    password = ""
    for i in range(8):
        random_char = chr(randint(40, 126))
        password += random_char
    return password

def is_valid_password(password):
    if not password:
        return False
    if len(password) != 8:
        return False

    big = False
    small = False
    num = False

    for ch in password:
        if ch.isupper():
            big = True
        elif ch.islower():
            small = True
        elif ch.isdigit():
            num = True
    return big and small and num
    
def get_password():
    max_attempts = 100
    attempts = 0
    while attempts < max_attempts:
        password = get_random_password()
        if is_valid_password(password):
            return password
        attempts += 1
    

print(get_password())


