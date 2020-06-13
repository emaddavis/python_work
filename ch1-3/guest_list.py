guest_list = ['Dali', 'Gaga', 'Warhol']

print(f"Hey, {guest_list[0]}, come by and grab a bite.")
print(f"Hey, {guest_list[1]}, come by and grab a bite.")
print(f"Hey, {guest_list[2]}, come by and grab a bite.")

cannot_attend = 'Gaga'

print(f"{cannot_attend} cannot attend")

print(guest_list[1])
guest_list[1] = 'Turner'

print(f"Hey, {guest_list[0]}, come by and grab a bite.")
print(f"Hey, {guest_list[1]}, come by and grab a bite.")
print(f"Hey, {guest_list[2]}, come by and grab a bite.")

print(f"{len(guest_list)} guests are attending")


print('We just found a bigger table')

guest_list.insert(0, 'Motzart')
guest_list.insert(2, 'Lennon')
guest_list.append('Allman')

print(f"Hey, {guest_list[0]}, come by and grab a bite.")
print(f"Hey, {guest_list[1]}, come by and grab a bite.")
print(f"Hey, {guest_list[2]}, come by and grab a bite.")
print(f"Hey, {guest_list[3]}, come by and grab a bite.")
print(f"Hey, {guest_list[4]}, come by and grab a bite.")
print(f"Hey, {guest_list[5]}, come by and grab a bite.")

print(f"{len(guest_list)} guests are attending")

print("The restraunt burnt down, I'm hosting, only two people can come")

uninvited = guest_list.pop()
print(f"Sorry, {uninvited}, you cannot come to dinner.")
uninvited = guest_list.pop()
print(f"Sorry, {uninvited}, you cannot come to dinner.")
uninvited = guest_list.pop()
print(f"Sorry, {uninvited}, you cannot come to dinner.")
uninvited = guest_list.pop()
print(f"Sorry, {uninvited}, you cannot come to dinner.")

print(f"Hey, {guest_list[0]}, come by and grab a bite.")
print(f"Hey, {guest_list[1]}, come by and grab a bite.")

print(f"{len(guest_list)} guests are attending")

del guest_list[0]
del guest_list[0]

print(guest_list)

print(f"{len(guest_list)} guests are attending")