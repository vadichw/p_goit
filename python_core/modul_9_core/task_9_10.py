# Створіть функцію get_favorites(contacts), яка повертатиме список, який містить лише обрані контакти. Використовуйте при цьому функцію filter, щоб відфільтрувати по полю favorite лише обрані контакти.

def get_favorites(list_contacts):
    new = list(filter(lambda contact: contact['favorite'], list_contacts ))
    return new

print(get_favorites([{
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": True,
},]))