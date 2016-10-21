cars = 100
spcae_in_a_car = 4.0
driver = 30
passengers = 90
cars_not_driven = cars - driver
cars_driven = driver
carpool_capacity = cars_driven * spcae_in_a_car
print("there are " + str(cars) + " cars available")
print("there are ", cars , " cars available" , sep="-")
values=(cars , "cars")
f="there are %d %s available" % values
print(f)