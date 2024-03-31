# Напишіть функцію real_len, яка підраховує та повертає довжину рядка без наступних керівних символів: ['\n', '\f', '\r', '\t', '\v']
# Test: 'Alex\nKdfe23\t\f\v.\r'

def real_len(text):
    sym =['\n', '\f', '\r', '\t', '\v']
    length = 0

    for element in text:
        if element not in sym:
            length = length + 1
    return length

real = real_len('Alex\nKdfe23\t\f\v.\r')
print(real)


