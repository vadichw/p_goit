# її довжина більша або дорівнює одному символу
# вона повністю складається з цифр
# передбачити виняток, що, можливо, є початковий знак "+" або "-", після якого мають йти цифри

def is_integer(s):
    
    if len(s) == 0:
        return False
    new = s.strip()

    return bool(new and (new[0] in '+-' or new.isdigit()))