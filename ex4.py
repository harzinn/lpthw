cars = 100
space_in_a_car = 4
drivers = 31
passengers = 300
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven
max_passegners_per_car = carpool_capacity / cars_driven
pissed_off_passengers = passengers - carpool_capacity


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,
    "in each car.")
print("But in reality, we will get", max_passegners_per_car, "per car.")
print("There will be", pissed_off_passengers, "passengers still needing a ride")
