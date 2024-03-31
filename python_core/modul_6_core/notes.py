#'r'	відкриття на читання (є значенням за замовчуванням).
#'w'	відкриття на запис, вміст файлу видаляється, якщо файлу не існує, створюється новий.
#'x'	відкриття на запис, якщо файлу не існує, інакше виняток.
#'a'	відкриття на дозапис, інформація додається в кінець файлу.
#'b'	відкриття у двійковому режимі.
#'t'	відкриття в текстовому режимі (є значенням за замовчуванням).
#'+'	відкриття на читання та запис


# fh = open('text.txt', 'w')
# sym_wr = fh.write('hello,world')
# print(sym_wr)
#  ЗАКРЫТЬВАТЬ ОБЯЗАТЕЛЬНО
#  fh.close()



## Read() and Write()

# fh = open('lecture_1.txt', 'r')
# while True:
#     line = fh.readlines()
#     if not line:
#         break
#     print(line)
# fh.close()


# Navigation, seek()
# Python дає можливість управляти положенням курсора у файлі, можна довільно переміщатися файлом за допомогою методу seek. Цей метод приймає один аргумент — це кількість символів, на які потрібно змістити курсор у файлі

fh = open('test.txt', 'w+')
fh.write('hello!')

fh.seek(1)
second = fh.read(1)
print(second)  # 'e'

fh.close()

# Щоб дізнатися положення курсора в цей момент, можна скористатися методом tell, він повертає позицію (номер) символу з початку файлу, де зараз знаходиться курсор.

fh = open('test.txt', 'w+')
fh.write('hello!')

position = fh.tell()
print(position) # 6

fh.seek(1)
position = fh.tell()
print(position) # 1

fh.read(2)
position = fh.tell()
print(position) # 3

fh.close()


# За своєю суттю байт-рядки або простіше байти — це звичайні рядки, але для запису одного символу використовується суворо один байт.

# Байт — це одиниця зберігання та обробки цифрової інформації, що містить 8 біт інформації. Один біт — це 0 або 1. За допомогою одного байта можна записати будь-яке число від 0 до 255 включно.

# Python за замовчуванням використовує UTF-8, в якій один символ може займати від 1 до 4 байт, і всього в алфавіті може бути до 1 112 064 знаків

byte_string = b'Hello'
#print(byte_string)

byte_word = 'Hello'.encode()
#print(byte_word)

numbers = [0, 128, 255]
byte_numbers = bytes(numbers)
print(byte_numbers)


byte_array = bytearray(b'Vadim Chepik')
byte_array[0] = ord('V')
byte_array[1] = ord('C')
print(byte_array)
