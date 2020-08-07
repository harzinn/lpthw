#where the magic happens
def magic(arg1):
    max = 180
    shards = max / 5
    shards1 = shards * 90
    total = arg1 * shards1
    return total

characters = int(input("How many characters are we checking?\n"))
howmany = magic(characters)
print(f"You would recieve {howmany} ultimus orb shards.\m")

characters2 = int(input("Again, How many characters are we checking?\n"))
howmany2 = magic(characters2)
print(f"You would recieve {howmany2} ultimus orb shards.\m")
