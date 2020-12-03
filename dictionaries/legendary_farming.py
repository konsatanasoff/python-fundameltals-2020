mapper = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}

key_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}


while True:
    sequence = input().split()
    is_found = False

    for index in range(0, len(sequence), 2):
        quantity = int(sequence[index])
        item = sequence[index + 1].lower()

        if item in key_materials:
            key_materials[item] += quantity
        else:
            if item not in junk:
                junk[item] = quantity
            else:
                junk[item] += quantity

        for key, value in key_materials.items():
            if value >= 250:
                print(f"{mapper[key]} obtained!")
                key_materials[key] -= 250
                is_found = True
                break

        if is_found:
            break

    if is_found:
        break

ordered_materials = sorted(key_materials.items(), key=lambda x: (-x[1], x[0]))

for item, quantity in ordered_materials:
    print(f"{item}: {quantity}")

ordered_junk = sorted(junk.items(), key=lambda x: x[0])
for junk_item, junk_quantity in ordered_junk:
    print(f"{junk_item}: {junk_quantity}")