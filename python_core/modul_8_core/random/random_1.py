from datetime import datetime, timedelta
import random

def get_random_birthday(n):
    current_date = datetime.now()
    oldest_date = current_date - timedelta(days=365*80)
    birth_days_list = []

    for i in range(n):
        fake_year = random.randrange(oldest_date.year, current_date.year)
        fake_month = random.randint(1, 12)
        fake_day = random.randint(1,31)
        try:
            fake_birthday = datetime(year=fake_year, month=fake_month, day=fake_day)
        except ValueError:
            continue
        if current_date >= fake_birthday:
            birth_days_list.append(fake_birthday.date())
    return birth_days_list





if __name__ == '__main__':
    birth_days_list = (get_random_birthday(10))
    #print(random.sample(birth_days_list, k= 2))
    data = [1,2,3,4,5]
    random.shuffle(data)
    print(data)