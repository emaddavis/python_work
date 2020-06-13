cars = ['bmw', 'audi', 'toyota', 'subaru']

#Length of list
print(len(cars))

#Chronologically reversing a list
print(cars)
cars.reverse()
print(cars)

#Temporary sorting
print(f"Here is the original list: {cars}")
print(f"Here is the list sorted in alphabetical order: {sorted(cars)}")
print(f"Here is the list sorted in reverse alphabetical order: {sorted(cars,reverse = True)}")
print(f"Here is the original list: {cars} \n")

#Perminantly sort barnds in alphabetical order
cars.sort()
print(cars)

#Perminantly osrt brands in reverse alphabetical order
cars.sort(reverse=True)
print(cars)