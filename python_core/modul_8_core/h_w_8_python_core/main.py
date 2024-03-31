from datetime import date, datetime, timedelta
from collections import defaultdict

def get_birthdays_per_week(users):

    user_list = defaultdict(list)

    current_day = date.today()
    current_year = current_day.year

    week_interval = timedelta(days=7)

    if not users:
        return {}
    
    for dict in users:
        user_birthday = dict.get('birthday')

        if user_birthday.month == 1:
            user_birthday = user_birthday.replace(year=current_year + 1)
        else:
            user_birthday = user_birthday.replace(year = current_year)

        if (current_day - user_birthday  > week_interval) or (user_birthday < current_day):
            continue

        birthday_weekday = user_birthday.weekday()

        if birthday_weekday not in (5,6):
            user_list[user_birthday.strftime('%A')].append(dict.get('name'))
        else:
            user_list['Monday'].append(dict.get('name'))

    return user_list


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 12, 3).date()},
        {"name": "Vadim", "birthday": datetime(2001, 12, 4).date()},
        {"name": "Vika", "birthday": datetime(2002, 12, 5).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)

    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")


# Импортируются необходимые модули: date, datetime, timedelta из модуля datetime и defaultdict из модуля collections.
# Определяется функция get_birthdays_per_week(users).
# Создается пустой defaultdict с именем users_list. defaultdict - это подкласс словаря, предоставляющий значение по умолчанию для несуществующего ключа.
# Получается текущая дата с использованием date.today().
# Извлекается текущий год из текущей даты.
# Определяется объект timedelta с именем week_interval, представляющий собой продолжительность недели.
# Проверяется, если длина списка users меньше 1. В случае успеха возвращается пустой словарь.
# Итерируется по каждому словарю в списке users.
# a. Извлекается день рождения пользователя из словаря.
# b. Проверяется, если месяц дня рождения пользователя — январь. Если это так, обновляется год дня рождения пользователя на следующий; в противном случае сохраняется текущий год.
# c. Проверяется, находится ли день рождения пользователя в течение следующей недели или уже прошел. В противном случае переходится к следующему пользователю.
# d. Определяется день недели дня рождения пользователя.
# e. Если день рождения не приходится на субботу (5) или воскресенье (6), добавляется имя пользователя к соответствующему ключу дня недели в словаре users_list. В противном случае добавляется имя пользователя к ключу "Monday".
# Возвращается словарь users_list, содержащий дни недели в качестве ключей и списки имен пользователей в качестве значений.