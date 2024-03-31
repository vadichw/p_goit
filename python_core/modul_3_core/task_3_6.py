# Створіть функцію format_string для форматування рядка. У функцію ми передаємо рядок string та length довжину нового рядка. Функція повертає новий рядок за наступним алгоритмом:
#Якщо довжина вихідного рядка більша або дорівнює length, ми повертаємо його в тому ж вигляді;
#Якщо вона менша length, ми додаємо попереду рядка пробіли в кількості (length - len(string)) // 2.

def format_string(length=15, string='abaa'):
    if len(string) >= length:
        return string
    else:
        spaces = (length - len(string)) // 2
        return ((' ' * spaces) + string)
    
print(format_string())