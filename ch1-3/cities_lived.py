cities = ['lynchburg', 'london', 'tampa', 'jakarta', 'dallas']

cities.append('Seattle')
cities.append('las vegas')
cities.remove('las vegas')
print(f"I would like to experience {cities.pop()}")

cities.insert(2, 'san fancisco')
print(f"I would like to experience {cities.pop(2).title()}")

print(f"I have lived in {len(cities)} cities")

print(f"Living in {cities[0]} was fun")


print('now for some fun with sorting')

print(sorted(cities))
print(sorted(cities,reverse = True))

cities.reverse()
print(cities)

cities.sort()
print(cities)

cities.sort(reverse = True)
print(cities)

print(cities[-1])