from Pet import Pet

pet1 = Pet("Tom", "Dog")
pet2 = Pet("Buster", "Parrot")
pet3 = Pet("Dog", "Cat")

print(pet1.name)
print(pet1.type)
print(pet1.hunger)
print(pet1.happiness)
print(pet1.bond)

print("What do you want to do?")
print("Feed")
print("Play")
print("Pet")

action = input()

while action != "Feed" and action != "Play" and action != "Pet":
    print("Sorry, try again!")
    action = input()