def token_parser(s):
    tokens = []  # список для зберігання лексем
    current_token = ''  # змінна для формування поточної лексеми

    # Проходимо по кожному символу в рядку
    for char in s:
        # Якщо символ - оператор або дужка, додаємо поточну лексему до списку і додаємо символ як нову лексему
        if char in "+-*/()":
            if current_token:
                tokens.append(current_token)
                current_token = ''
            tokens.append(char)
        # Якщо символ - цифра, додаємо його до поточної лексеми
        elif char.isdigit():
            current_token += char
        # Якщо символ - прогалина, додаємо поточну лексему до списку і очищуємо поточну лексему
        elif char == ' ':
            if current_token:
                tokens.append(current_token)
                current_token = ''

    # Додаємо залишкову лексему, якщо вона є
    if current_token:
        tokens.append(current_token)

    return tokens


#############

# import re
#
#
# def tokenize_expression(expression):
#     # Використовуємо регулярний вираз для виділення чисел, операторів та дужок
#     tokens = re.findall(r'\d+|[-+*/()]', expression)
#
#     # Видаляємо можливі прогалини
#     tokens = [token.strip() for token in tokens if token.strip()]
#
#     return tokens
