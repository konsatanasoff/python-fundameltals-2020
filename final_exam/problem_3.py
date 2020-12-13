def add(data, person, h, e):
    if person in data:
        data[person]['health'] += h
    else:
        data[person] = {'health': h, 'energy': e}


def attack(data, attacker, defender, damage):
    if attacker in data and defender in data:
        data[defender]['health'] -= damage
        data[attacker]['energy'] -= 1

        if data[defender]['health'] <= 0:
            del data[defender]
            print(f"{defender} was disqualified!")

        if data[attacker]['energy'] <= 0:
            print(f'{attacker} was disqualified!')
            del data[attacker]
    return data


def delete():
    pass


line = input()

person_data = {}

while not line == "Results":
    action = line.split(":")[0]

    if action == "Add":
        person, health, energy = line.split(":")[1:]
        health = int(health)
        energy = int(energy)
        add(person_data, person, health, energy)

    elif action == "Attack":
        attacker, defender, damage = line.split(":")[1:]
        damage = int(damage)
        person_data = attack(person_data, attacker, defender, damage)

    elif action == "Delete":
        person = line.split(":")[1]
        if person in person_data:
            del person_data[person]
        elif person == "All":
            person_data.clear()

    line = input()

print(f"People count: {len(person_data)}")

sorted_data = dict(sorted(person_data.items(), key=lambda x: (-x[1]['health'], x[0])))

for person, data in sorted_data.items():
    print(f"{person} - {data['health']} - {data['energy']}")
