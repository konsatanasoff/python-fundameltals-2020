def plunder(cities, town, people, gold):
    cities[town]['population'] -= people
    cities[town]['gold'] -= gold
    print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
    if cities[town]['population'] == 0 or cities[town]['gold'] == 0:
        del cities[town]
        print(f"{town} has been wiped off the map!")

    return cities


def prosper(cities, town, gold):
    if gold > 0:
        cities[town]['gold'] += gold
        print(f"{gold} gold added to the city treasury. {town} now has {cities[town]['gold']} gold.")
    else:
        print("Gold added cannot be a negative number!")
    return cities


command = input()

cities = {}
while not command == "Sail":
    city, population, gold = command.split("||")
    population = int(population)
    gold = int(gold)
    if city not in cities:
        cities[city] = {'gold': gold, 'population': population}
    else:
        cities[city]['gold'] += gold
        cities[city]['population'] += population
    command = input()

command = input()

while not command == "End":
    action = command.split("=>")[0]

    if action == "Plunder":
        town, people, gold = command.split("=>")[1:]
        people = int(people)
        gold = int(gold)
        cities = plunder(cities, town, people, gold)

    elif action == "Prosper":
        town, gold = command.split("=>")[1:]
        gold = int(gold)
        cities = prosper(cities, town, gold)

    command = input()

sorted_cities = sorted(cities, key=lambda x: (-cities[x]['gold'], x))

print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")

for city in sorted_cities:
    print(f"{city} -> Population: {cities[city]['population']} citizens, Gold: {cities[city]['gold']} kg")
