text = 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor.'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
words = []
start = 0
# = text.split() # Засунет каждое слово в список как отдельный елемент
for indx, char in enumerate(text):
    if not char.lower() in alphabet: 
        # Напечает символ только когда он есть в алфавите. 
        # Если добавить НЕ после ИФ то можна увидеть те символы которые не входят в алфавит, в этом случае - пробелы
        #print(indx, char)
        word = text[start:indx]
        words.append(word.strip())
        start = indx
print(words)