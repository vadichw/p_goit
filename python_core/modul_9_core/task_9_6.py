# Нехай є рядок з числами (з метою спрощення числа лише цілі), що визначає якісь частини загального доходу. Наприклад,
# "The resulting profit was: from the southern possessions $ 100, from the northern colonies $500, and the king gave $1000."
# Необхідно реалізувати функцію generator_numbers, яка буде парсити рядок і знаходити всі цілі числа в ньому та працювати як генератор, який буде віддавати зазначені числа при зверненні до нього у циклі.

# З парсингом рядків ми вже зіштовхувалися виконуючи завдання модуля 7, коли розбивали на лексеми арифметичний вираз

# Функція generator_numbers(string="") безпосередньо розпарсює рядок і за допомогою yield повертає поточне число.

# Функція sum_profit(string) підсумовує числа, отримані від generator_numbers, та повертає загальну суму прибутку з рядка.

def generator_numbers(string=""):
    current_number = ""
    for char in string:
        if char.isdigit():
            current_number += char
            
        elif current_number:
            yield int(current_number)
            current_number = ""
    
    if current_number:
        yield int(current_number)


def sum_profit(string):
    total_profit = sum(generator_numbers(string))
    return total_profit


print(sum_profit("The resulting profit was: from the southern possessions $ 100, from the northern colonies $500, and the king gave $1000."))