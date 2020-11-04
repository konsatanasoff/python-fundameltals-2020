def shoot(action, my_list, start, length, points):
    if start in range(len(my_list)):
        if action.split()[1] == "Left":
            index = (start - length) % len(my_list)

        elif action.split()[1] == "Right":
            index = (start + length) % len(my_list)

        if my_list[index] <= 5:
            points += my_list[index]
            my_list[index] = 0

        else:
            points += 5
            my_list[index] -= 5

    return my_list, points


def reverse(my_list):
    my_list = my_list[::-1]

    return my_list


targets = list(map(int, input().split("|")))
command = input()

points = 0

while not command == "Game over":
    action = command.split("@")[0]

    if action == "Shoot Left" or action == "Shoot Right":
        start_index = int(command.split("@")[1])
        length = int(command.split("@")[2])

        if start_index <= len(targets):
            targets, points = shoot(action, targets, start_index, length, points)

    elif action == "Reverse":
        targets = reverse(targets)

    command = input()

print(" - ".join(map(str, targets)))
print(f"Iskren finished the archery tournament with {points} points!")