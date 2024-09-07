cars = ["opel","mercedes","mazda","bmw"]

print(len(cars))

print(cars[0], cars[3])

cars[3] = "toyota"
print(cars)

result = "mercedes" in cars
print(result)

#son iki eleman değişecek!
cars = cars + ["renault","toyota"]
r = cars
print(r)

cars_2 = cars + ["tesla", "nissan"]
print(cars_2)


del cars[-1]
print(cars)
