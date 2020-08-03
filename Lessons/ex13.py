from sys import argv
# read the WYSS section for how to run this
script, lastname, second, third, fourth = argv

name = input("What is your name?")

print(f"Hi, {name}!")
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is", second)
print("Your third variable is", third)
print("Your 4th variable is", fourth)
