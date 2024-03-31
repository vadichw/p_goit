def caching_fibonacci():
        cache = {}

    # Внутрішня рекурсивна функція для обчислення числа Фібоначчі
        def fibonacci(n):
        # Перевірка, чи число вже є в кеші
            if n in cache:
                return cache[n]
        
        # Базовий випадок: якщо n рівне 0 або 1
            if n == 0:
                result = 0
            elif n == 1:
                result = 1
            else:
            # Рекурсивно викликаємо функцію для обчислення числа
                result = fibonacci(n - 1) + fibonacci(n - 2)

        # Зберігаємо обчислене значення в кеші
            cache[n] = result

        # Повертаємо обчислене значення
            return result

    # Повертаємо функцію fibonacci, яка має доступ до кешу
        return fibonacci
    
