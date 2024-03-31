import sys
from main import main as greeting
from final import main as exiting



def main():
    try:
        if sys.argv[1] == 'greet':
            greeting()

        elif sys.argv[1] == 'goodbuy':
            exiting()
        print(sys.argv)
        
    except IndexError:
        print("greet or goodbuy")








if __name__ == "__main__":
    main()