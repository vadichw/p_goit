from datetime import datetime


def get_str_date(date):
    # strptime
    # Перетворення рядкового представлення дати в об'єкт datetime
    datetime_obj = datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%fZ')
    
    # strftime
    # Форматування дати в новий рядок
    formatted_date = datetime_obj.strftime('%A %d %B %Y')

    return formatted_date

print(get_str_date('2021-05-27 17:08:34.149Z'))