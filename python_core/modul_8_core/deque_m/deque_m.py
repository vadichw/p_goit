from collections import deque

# def main():
#     queue = deque(maxlen=10)
#     for i in range(21):
#         queue.append(i)
#     start = queue.popleft()
#     end = queue.pop()
#     print(start)
#     print(end)

# if __name__ == '__main__':
#     main()
    
def main():
    #user_results = []
    user_results = deque(maxlen=3)
    while True:
        user_input = input("Enter ")
        user_results.append(user_input)
        if user_input == 'q':
            break
        
    print("Bye")
    print(f"User steps are {user_results}")


if __name__ == '__main__':
    main()