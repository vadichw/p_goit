import csv


def write_contacts_to_file(filename, contacts):
    # Визначаємо заголовки
    fieldnames = ["name", "email", "phone", "favorite"]

    with open(filename, 'w', newline='') as file:
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writeheader()

        # Записуємо кожен контакт у файл
        for contact in contacts:
            csv_writer.writerow({
                "name": contact["name"],
                "email": contact["email"],
                "phone": contact["phone"],
                "favorite": contact["favorite"]
            })


def read_contacts_from_file(filename):
    contacts = []
    with open(filename, 'r', newline='') as file:
        spam_reader = csv.reader(file)
        next(spam_reader)
        for row in spam_reader:
            name, email, phone, favorite_str = row
            favorite = True if favorite_str == 'True' else False
            contacts.append({'name': name, 'email': email, 'phone': phone, 'favorite': favorite})
        return contacts