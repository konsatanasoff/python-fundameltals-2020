def include(my_list, shop):
    my_list.append(shop)
    return my_list


def visit(my_list, pos, n_shops):
    if pos == "first" and n_shops <= len(my_list):
        for _ in range(n_shops):
            my_list.pop(0)
    elif pos == "last" and n_shops <= len(my_list):
        for _ in range(n_shops):
            my_list.pop()
    return my_list


def prefer(my_list, i_1, i_2):
    if i_1 < len(my_list) and i_2 < len(my_list):
        my_list[i_2], my_list[i_1] = my_list[i_1], my_list[i_2]
    return my_list


def place(my_list, shop, i):
    if i < len(my_list):
        my_list.insert(i+1, shop)
    return my_list


shop_list = input().split()
n_commands = int(input())

for _ in range(n_commands):
    command = input()
    action = command.split()[0]

    if action == "Include":
        shop = command.split()[1]
        shop_list = include(shop_list, shop)

    elif action == "Visit":
        position_to_remove = command.split()[1]
        n_shops = int(command.split()[2])
        shop_list = visit(shop_list, position_to_remove, n_shops)

    elif action == "Prefer":
        index_1 = int(command.split()[1])
        index_2 = int(command.split()[2])
        shop_list = prefer(shop_list, index_1, index_2)

    elif action == "Place":
        shop = command.split()[1]
        index = int(command.split()[2])
        shop_list = place(shop_list, shop, index)

print("Shops left:")
print(" ".join(shop_list))
