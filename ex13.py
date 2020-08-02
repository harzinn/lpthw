from sys import argv
# read the WYSS section for how to run this
script, lastname = argv

name = input("What is your first name?")

print(f"Hi, {name}!")
print(f"I suppose your full name would be {name} {lastname} wouldn't it?")
