motercycles = ['honda', 'yamaha', 'suzuki']

#Modifying elements in a list
print(motercycles)
motercycles[0] = 'ducati'
print(motercycles)

#Adding elements to a list
motercycles.append('honda')
print(motercycles)

#Inserting an element into a list
motercycles.insert(0, 'harley')
print(motercycles)

#Removing an element into a list
del motercycles[0]
print(motercycles)

#Removing an element from a list based on value
too_expensive = 'ducati'
motercycles.remove(too_expensive)
print(motercycles)

#Popping the last element of a list
popped_motercycle = motercycles.pop()
print(motercycles)
print(popped_motercycle)

#Popping a specific location from a list
first_motercycle = motercycles.pop(0)
print(motercycles)
print(first_motercycle)
