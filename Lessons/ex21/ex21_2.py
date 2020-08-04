#Tuesday, August 4, 2020 6:53 PM
def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a* b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b


print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


#A puzzle for extra credit, type it in anyway.
print("Here is a puzzle")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes", what, "Can you do it by hand?\n\n")

test = 24 + 34 / 100 - 1023

val1 = 34 / 100
val2 = val1 + 24
val3 = val2 - 1023

val11 = divide(34, 100)
val12 = add(val11, 24)
val13 = subtract(val12, 1023)

#Come back to this later and fix it, trying to do one line math for the formula
result = subtract(1023, add(34, divide(34, 100)))

print(result) #this result is coming up positive for some reason
print(val13)
print(val3)
print(test)
