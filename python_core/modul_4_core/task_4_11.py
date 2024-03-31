def is_valid_password(password):
    if not password:
        return False
        
    if len(password) !=8:
        return False
        
    upper = any(char.isupper() for char in password)
    lower = any(char.islower() for char in password)
    digit = any(char.isdigit() for char in password)

    return upper and lower and digit