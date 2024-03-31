from pathlib import Path
import sys

def main():
    if len(sys.argv) < 2:
        user_input = ""
    else:
        user_input = sys.argv[1]

    path = Path(user_input)

    if path.exists():
        if path.is_dir():
            items = path.iterdir()
            #items = path.glob("*.py")
            for item in items:
                print(item)
        else:
            print(f"{path} is a file")
    else:
        print(f"{path.absolute()} doesn`t exist")




if __name__ == "__main":
    main()