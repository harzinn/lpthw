def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

#my own custom function
def silverware(forks, knives, spoons):
    print(f"You have {spoons} spoons, {knives} knives, and {forks} forks.")
    print("If we devide the amount of spoons we have by three...")
    spoons_3 = spoons / 3
    print(f"We get {spoons_3} !\n\n")

#call the function with hard coded numbers
silverware(15, 13, 17)

#ask user for input about forkies, knifies, and spoonies and then...
#convert said input to intergers to allow silverware function to math it
spoons_input = int(input("How many spoons do we have?\n"))
forks_input = int(input("How many forks do we have?\n"))
knives_input = int(input("How many knives do we have?\n"))

#run the function again with the input from the user
silverware(spoons_input, forks_input, knives_input)


print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)


print("Or we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
cheese_and_crackers(10 +20, 5+6)


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
