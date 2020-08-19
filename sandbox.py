def program(max, steps):
    i = 0
    numbers = []

    print(f"At the top i is {i}")
    numbers = [*range(0, max, steps)]

    i = i + steps
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")


    print("The numbers: ")

    for x in numbers:
        print(x)

top_end = int(input("Max range number:> "))
increment_by = int(input("Increment by how many?:> "))

program(top_end, increment_by)
