#where the magic happens
def magic(arg1):
    x = 180
    shards = x / 5
    shards1 = shards * 90
    total = arg1 * shards1
    return total

#goal is to pass data to the function magic more than one &
#and get different (or same) results

#lets make some magic
characters = int(input("How many characters are we checking?\n"))
howmany = magic(characters)
print(f"You would recieve {howmany} ultimus orb shards.\m")

#lets make more magic
characters2 = int(input("Again, How many characters are we checking?\n"))
howmany2 = magic(characters2)
print(f"You would recieve {howmany2} ultimus orb shards.\m")

#done
