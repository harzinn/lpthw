from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

#seek moves characters, not lines
def rewindish(f):
    f.seek(3)

#line_count and f are both variables we are passing things into
#line_count is passed into from current line, f is the file
def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("first let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.\n")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

#reset the current lines
current_line = 1

#mostly rewind the input_file
rewindish(current_file)

#now lets print it again
print("Let's see how far back we've gone")
print_a_line(current_line, current_file)
