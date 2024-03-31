# Створіть функцію get_random_winners(quantity, participants), яка повертатиме список унікальних ідентифікаторів бази даних зі словника participants в кількості quantity. Це буде список переможців
# Отримайте перелік ключів словника. (Після виконання методу keys() використовуйте перетворення типів)
# Перемішайте отриманий список за допомогою методу shuffle
# Виберіть випадкових переможців, використовуючи метод sample.
# Якщо передана кількість переможців більша за кількість користувачів (quantity > len(participants)) — поверніть порожній список.

import random

def get_random_winners(quantity, participants):
    if quantity > len(participants):
        return []

    participants_keys = list(participants.keys())
    random.shuffle(participants_keys)
    new_list = random.sample(participants_keys, k=quantity)
    return new_list
