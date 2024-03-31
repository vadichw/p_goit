# def greeting(mode):
#     if mode == 'm':
#         return hello_male
#     elif mode == 'f':
#         return hello_female

# def hello_male(name):
#     print(f"Mr.{name}")

# def hello_female(name):
#     print(f"Mrs {name}")

# def main():
#     mr = greeting('m')
#     mrs = greeting('f')

#     mr("Vadim")
#     mrs("Vika")

def hello_pan(name):
    print(f"Lord, {name}")

def hello_male(name):
    print(f"Mr.{name}")

def hello_female(name):
    print(f"Mrs {name}")
    
MODES = {'m': hello_male,
         'f': hello_female,
         'pan': hello_pan,}
         
def greeting(mode):
    return MODES[mode]

    
def main():
    mr = greeting('m')
    mrs = greeting('f')
    pan = greeting('pan')

    mr("Vadim")
    mrs("Vika")
    pan('Taras')




if __name__ == "__main__":
    main()