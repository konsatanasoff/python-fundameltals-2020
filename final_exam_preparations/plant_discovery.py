n_lines = int(input())

plants = {}

for _ in range(n_lines):
    plant, rarity = input().split('<->')
    rarity = int(rarity)
    plants[plant] = {'rarity': rarity, 'rating': []}

command = input()

while not command == "Exhibition":
    action, data = command.split(": ")
    try:
        if action == "Rate":
            plant, new_rating = data.split(' - ')
            new_rating = int(new_rating)
            plants[plant]['rating'].append(new_rating)

        elif action == "Update":
            plant, new_rarity = data.split(' - ')
            new_rarity = int(new_rarity)
            plants[plant]['rarity'] = new_rarity

        elif action == "Reset":
            plant = data
            plants[plant]['rating'].clear()
    except:
        print("error")

    command = input()

for plant_name, plants_data in plants.items():
    if plants[plant_name]['rating']:
        plants[plant_name]['avg'] = sum(plants[plant_name]['rating'])/len(plants[plant_name]['rating'])
    else:
        plants[plant_name]['avg'] = 0

sorted_plants = sorted(plants.items(), key=lambda x: (x[1]['rarity'], x[1]['avg']), reverse=True)

print("Plants for the exhibition:")
for plant_name, value in sorted_plants:
    print(f"- {plant_name}; Rarity: {value['rarity']}; Rating: {value['avg']:.2f}")

