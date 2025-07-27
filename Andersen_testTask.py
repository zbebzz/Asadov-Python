taskSelector = int(input("Please choose the task (type '1' or '2'): "))


if taskSelector == 1:
    # task 1.1
    num1 = int(input("Please enter a number: "))
    if (num1 > 7):
        print("Hello")

    # task 1.2
    name = input("Please enter a name: ")
    if (name == "John"):
        print("Hello, John")
    else:
        print("There is no such name")

    # task 1.3
    inputArray = input("Please enter numbers separated by space: ")
    numbers = list(map(int, inputArray.split())) 
    print("Numbers that are multiples of 3: ")
    # for num in numbers:
    #     if num % 3 == 0:
    #         print(num)
    print(*[num for num in numbers if num % 3 == 0])


if taskSelector == 2:
    # task 2
    print("\nCan the following bracket sequence be considered correct?\n[((())()(())]]") 
    print("\nAnswer: No, it cannot, since the respective pairs " \
        "of brackets do not match.\n" \
        "In order to balance it, the missing '[' and ')' brackets need " \
        "to be added to the sequence.\nThe final correct sequence is " \
        "[[((())()(()))]].")
