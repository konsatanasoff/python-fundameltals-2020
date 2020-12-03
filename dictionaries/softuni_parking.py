def register(name, plate, my_dict):
    if name not in my_dict:
        my_dict[name] = plate
        print(f"{name} registered {my_dict[name]} successfully")
    else:
        print(f"ERROR: already registered with plate number {my_dict[name]}")

    return my_dict


def unregister(name, my_dict):
    if name in my_dict:
        print(f"{name} unregistered successfully")
        del my_dict[name]
    else:
        print(f"ERROR: user {name} not found")

    return my_dict


n_lines = int(input())

plate_data = {}

for _ in range(n_lines):
    line = input().split()
    action = line[0]

    if action == "register":
        name = line[1]
        plate = line[2]
        plate_data = register(name, plate, plate_data)

    elif action == "unregister":
        name = line[1]
        plate_data = unregister(name, plate_data)

for name, plate in plate_data.items():
    print(f"{name} => {plate}")
