def get_name():
    name = input("Enter name ")
    return name

def greet(name):
    print(f"Hello, my Lord {name}")

def main():
    name = get_name()
    greet(name)

# ENTRY POINT 
# ЧТОБ В 2ом файле НЕ ВЫЗЫВАЛСЯ ФУНКЦИОНАЛ 1го
#if __name__ == "__main__":
    #main()