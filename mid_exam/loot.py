def loot(my_list, items):
    for item in items:
        if item not in my_list:
            my_list.insert(0, item)
    return my_list


def drop(my_list, i):
    if 0 <= i < len(my_list):
        saved_item = my_list[i]
        my_list.pop(i)
        my_list.append(saved_item)
    return my_list


def steal(my_list, count):
    if count > len(my_list):
        removed = my_list.copy()
        count = len(my_list)

    else:
        removed = my_list[::-1]
        removed = list(reversed(removed[0:count]))

    for i in range(1, count + 1):
        my_list.pop()


    print(", ".join(removed))

    return my_list


treasure_chest = input().split("|")
command = input()

while not command == "Yohoho!":
    action = command.split()[0]

    if action == "Loot":
        items = command.split()[1:]
        treasure_chest = loot(treasure_chest, items)

    elif action == "Drop":
        index = int(command.split()[1])
        treasure_chest = drop(treasure_chest, index)

    elif action == "Steal":
        count = int(command.split()[1])
        treasure_chest = steal(treasure_chest, count)

    command = input()

count_items = len([el for el in treasure_chest])
total_elements = sum([len(el) for el in treasure_chest])

if count_items > 0:
    average_gain = total_elements / count_items
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")

else:
    print("Failed treasure hunt.")