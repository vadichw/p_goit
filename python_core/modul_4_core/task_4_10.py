from random import randint
#randon_num = randint(40, 126)

def get_random_password():

    password = ""

    for sym in range(8):
        random_char = chr(randint(40, 126))
        password = password + random_char
        
    return password

print(get_random_password())