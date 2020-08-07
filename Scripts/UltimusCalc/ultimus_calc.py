#calling functions practice and improvements Friday, August 7, 2020 2:46 PM

#where the magic happens
def magic(arg1):
    #check how many characters we are going to multiply the final total by
    characters = int(input("How many characters are we checking?\n"))
    #take the input of the function and run ultimus math on it
    x = arg1 / 5
    total = x * 90
    #take the total and then multiply it by the earlier character check
    real_total = total * characters
    #return the final total back to whatever called the function
    return real_total

#Take input from user on shard information
x = int(input("How many extra char shards will you recieve?\n"))
#pass input from user into magic fucntion and save as y
y = magic(x)
#print the results of the funcion return in the next line
print(f"You would recieve {y} ultimus orb shards.\n")
#poor attempt at letting the user read it before closing if ran double clicked
input("Press Enter to close")
