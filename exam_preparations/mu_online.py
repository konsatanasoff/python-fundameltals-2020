rooms = input().split('|')

health = 100
bitcoins = 0
best_room = 0
MAX_HEALTH = 100
is_killed = False
monster = ""

for room in rooms:
    command, number = room.split()
    number = int(number)
    best_room += 1

    if command == "potion":
        health += number

        if health <= MAX_HEALTH:
            print(f"You healed for {number} hp.")
            print(f"Current health: {health} hp.")

        else:
            print(f"You healed for {number - (health - MAX_HEALTH)} hp.")
            health = 100

            print(f"Current health: {health} hp.")

    elif command == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")

    else:
        health -= number
        if health > 0:
            print(f"You slayed {command}.")

        else:
            monster = command
            is_killed = True
            break


if is_killed:
    print(f"You died! Killed by {monster}.")
    print(f"Best room: {best_room}")
else:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")