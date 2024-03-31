from threading import Thread


# 1. Самый простой поток это функция
def worker(param):
    print(param)


if __name__ == "__main__":
    for i in range(5):
        th = Thread(target=worker, args=(f"Count thread - {i}",))
        th.start()

# Функция выполнилась 5 раз, но в отдельном потоке

