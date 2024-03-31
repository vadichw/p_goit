from pathlib import Path
def parse_folder(path):
    files = []
    folders = []

    for elements in path.iterdir():
        if elements.is_file():
            files.append(elements.name)
        elif elements.is_dir():
            folders.append(elements.name)
    return files, folders
    

# У Path є ряд корисних методів та атрибутів:

#p.parent вказує на батьківську теку;
#p.name повертає лише ім'я (рядок) теки або файлу, на який вказує p;
#p.is_dir() повертає True, якщо p вказує на теку, та False, якщо на файл або такий шлях не існує;
#.is_file() повертає True, якщо p вказує на файл, та False, якщо на теку, або такий шлях не існує;
#.iterdir() повертає ітератор по всіх файлах та теках усередині теки p;

