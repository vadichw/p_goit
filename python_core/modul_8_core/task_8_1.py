from datetime import datetime


def get_days_from_today(date):
    current_date = datetime.now()
    
    new_date = date.split('-')
    
    year = int(new_date[0])
    month = int(new_date[1])
    day = int(new_date[2])
    
    ch_date = datetime(year=year, month=month, day=day)
    
    d = (current_date - ch_date).days # Параметр .days витягає кількість днів з отриманої різниці.
    return d 

print(get_days_from_today("2023-11-01"))