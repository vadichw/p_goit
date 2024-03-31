import json


def write_contacts_to_file(filename, contacts):
    # Зберігаємо список контактів за ключем 'contacts' у файлі
    data_to_write = {'contacts': contacts}

    with open(filename, "w") as file:
        json.dump(data_to_write, file)

    return data_to_write  # Повертаємо дані, які були записані у файл


def read_contacts_from_file(filename):
    with open(filename, "r") as file:
        data = json.load(file)

    # Повертаємо список контактів, якщо він існує у зчитаних даних
    return data.get('contacts', [])


