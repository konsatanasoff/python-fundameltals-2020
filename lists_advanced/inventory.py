items = input().split(", ")
command = input()


def collect(list, item):
    if item not in list:
        list.append(item)
    return list


def drop(list, item):
    if item in list:
        list.remove(item)
    return list


def combine(list, items):
    old_item = items.split(":")[0]
    new_item = items.split(":")[1]

    if old_item in list:
        list.insert((list.index(old_item)) + 1, new_item)

    return list


def renew(list, item):
    if item in list:
        list.remove(item)
        list.append(item)

    return list


while not command == "Craft!":
    action, item = command.split(" - ")

    if action == "Collect":
        items = collect(items, item)

    elif action == "Drop":
        items = drop(items, item)

    elif action == "Combine Items":
        items = combine(items, item)

    elif action == "Renew":
        items = renew(items, item)

    command = input()

print(", ".join(items))