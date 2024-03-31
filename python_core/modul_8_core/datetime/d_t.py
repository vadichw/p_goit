from datetime import datetime

def get_days():
    #Скрипт який рахує кількість днів до заданої дати
    user_input = input("Enter data dd.mm ")

    user_date = datetime.strptime(user_input, '%d.%m')
    current_date = datetime.now()

    user_date = user_date.replace(year=current_date.year)
    delta_dates = user_date - current_date
    target_date = datetime.strftime(user_date, '%d-%B-%Y')
    if delta_dates.days > 0:
        print(f"{delta_dates.days} days left before {target_date}")
    else:
        user_date = user_date.replace(year=user_date.year + 1)
        delta_dates = user_date - current_date
        print(f"{delta_dates.days}days left before {target_date}")
    
    
# Тип название файла будет уникальным
# def make_backup(data):
#     current_date = datetime.now()
#     with open(f'backup_{current_date.timestamp()}.txt', 'w') as file:
#         file.write(data)   
    
    
if __name__ == "__main__":
    get_days()
    # data = 'abc'
    # make_backup(data)