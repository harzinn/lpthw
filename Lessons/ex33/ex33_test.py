<<<<<<< HEAD
def program(increment, max):
=======
def program():
    increment = 2
    max = 10
>>>>>>> 10bd0d096ad5a965f079b140c747e259378b4748
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
