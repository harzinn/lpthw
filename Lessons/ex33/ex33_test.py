def program(increment, max):
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

top_end = int(input("Max range number:> "))
increment_by = int(input("Increment by how many?:> "))

program(increment_by, top_end)
