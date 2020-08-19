def program():
    increment = 2
    max = 10
    i = 0
    numbers = []

    while i < max:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + increment
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


    print("The numbers: ")

    for x in numbers:
        print(x)

program()
