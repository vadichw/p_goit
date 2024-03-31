#import calendar
#from datetime import date

#def days_in_month(month, year):
    #try:
        #return calendar.monthrange(year, month)[1]
    #except ValueError:
        #return "Некоректний номер місяця або рік."

#print(days_in_month(2, 2004))


###


#def days_in_month(month, year):
    #if month < 1 or month > 12:
        #return "Некоректний номер місяця. Введіть число від 1 до 12."

    #elif month in {1, 3, 5, 7, 8, 10, 12}:
        #return 31
    #elif month in {4, 6, 9, 11}:
        #return 30
    # Умова (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) перевіряє, чи рік є високосним. Це стандартне правило: рік є високосним, якщо він ділиться на 4, але не ділиться на 100, за винятком випадків, коли він ділиться на 400. Якщо ця умова виконується, функція повертає 29, інакше - 28.
    # Це враховує правила високосних років та визначає кількість днів у лютому для заданого року.
    #elif month == 2:
        #return 29 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 28
    #else:
        #return "Невідомий місяць."
#print(days_in_month(2, 2005))

