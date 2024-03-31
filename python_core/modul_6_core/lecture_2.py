# Сортування файлів у папці
# Копіювати файли з папки та покласти в іншу з тим же розширеням

import argparse
from pathlib import Path
from shutil import copyfile


parser = argparse.ArgumentParser(description='Sorting folder')
# ім'я змінної
parser.add_argument('--source', '-s', required=True, help='source folder') 
# результативна папка
#parser.add_argument('--output', '-o', default='dist', help='output folder') 
args = vars(parser.parse_args()) # парсер vars поверне словник

source = args.get('source')
#output = source

# print(f"{args}")
# print(source, output)

# READ
def read_folder(path):
    for element in path.iterdir():
        if element.is_dir():
            read_folder(element)
        else:
            copy_file(element)

# COPY
def copy_file(file):
    ext = file.suffix.replace('.', '') # тут я прост удалил точки с названия папок 
    new_path = output_folder / ext
    new_path.mkdir(exist_ok = True, parents = True)
    copyfile(file, new_path/file.name)


output_folder = Path(source)
read_folder(Path(source))




