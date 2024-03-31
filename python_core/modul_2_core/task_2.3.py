num = int(input("Enter a number: "))

if num > 0:
    if num % 2 == 1:
        result = "Positive odd number"
        print(result)
    else:
        result = "Positive even number"
        print(result)
elif num < 0:
    result = "Negative number"
    print(result)

else:
    result = "It is zero"
    print(result)