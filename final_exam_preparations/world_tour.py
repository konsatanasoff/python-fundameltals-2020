def add_stop(data, i, string ):
    if i < len(data):
        left_side = data[:i]
        right_side = data[i:]
        data = left_side + string + right_side
    print(data)
    return data


def remove_stop(data, start, stop):
    if start < len(data) and stop < len(data):
        to_remove = data[start:stop + 1]
        data = data.replace(to_remove, '')
    print(data)
    return data


def switch(data, old, new):
    if old in data:
        data = data.replace(old, new)
    print(data)
    return data


cities = input()

command = input()

while not command == "Travel":
    action = command.split(":")[0]

    if action == "Add Stop":
        index, string = command.split(":")[1:]
        index = int(index)
        cities = add_stop(cities, index, string)
    elif action == "Remove Stop":
        start_index, stop_index = command.split(":")[1:]
        start_index = int(start_index)
        stop_index = int(stop_index)
        cities = remove_stop(cities, start_index, stop_index)
    elif action == "Switch":
        old_string, new_string = command.split(":")[1:]
        cities = switch(cities, old_string, new_string)

    command = input()

print(f"Ready for world tour! Planned stops: {cities}")
