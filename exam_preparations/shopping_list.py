shopping_list = input().split("!")
command = input()


def urgent(my_list, item):
    if item not in my_list:
        my_list.insert(0, item)

    return my_list


def unnecessary(my_list, item):
    if item in my_list:
        my_list.remove(item)

    return my_list


def correct(my_list, old_item, new_item):
    if old_item in my_list:
        old_index = my_list.index(old_item)
        my_list.insert(old_index, new_item)
        my_list.remove(old_item)

    return my_list


def rearrange(my_list, item):
    if item in my_list:
        my_list.remove(item)
        my_list.append(item)

    return my_list


while not command == "Go Shopping!":
    data = command.split()

    if data[0] == "Urgent":
        shopping_list = urgent(shopping_list, data[1])

    elif data[0] == "Unnecessary":
        shopping_list = unnecessary(shopping_list, data[1])

    elif data[0] == "Correct":
        shopping_list = correct(shopping_list, data[1], data[2])

    elif data[0] == "Rearrange":
        shopping_list = rearrange(shopping_list, data[1])

    command = input()

print(", ".join(shopping_list))