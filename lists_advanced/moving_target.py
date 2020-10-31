targets = input().split()
targets = list(map(int, targets))
command = input()


def shoot(targets, index, power):
    if 0 <= index < len(targets):
        targets[index] -= power
        if targets[index] <= 0:
            targets.pop(index)
    return targets


def add(targets, index, value):
    if 0 <= index < len(targets):
        targets.insert(index, value)
    else:
        print("Invalid placement!")
    return targets


def strike(targets, index, value):
    left_index = index - value
    right_index = index + value

    if left_index >= 0 and right_index < len(targets):
        left_part = targets[:left_index]
        right_part = targets[right_index + 1:]
        targets = left_part + right_part
    else:
        print("Strike missed!")

    return targets


while not command == "End":
    action, index, value = command.split()
    index = int(index)
    value = int(value)

    if action == "Shoot":
        targets = shoot(targets, index, value)

    elif action == "Add":
        targets = add(targets, index, value)

    elif action == "Strike":
        targets = strike(targets, index, value)

    command = input()

print("|" . join(map(str, targets)))