def fibonacci(n):
    if n in (1, 2):
        return 1
    elif n == 0:
        return 0 
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(10))
