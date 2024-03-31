def is_equal_string(utf8_string, utf16_string):
    
    utf8 = utf8_string.decode()
    utf16 = utf16_string.decode('utf16')

    if utf8 == utf16:
        return True
    return False