def swap(array_list, i_1, i_2):
    array_list[i_1], array_list[i_2] = array_list[i_2], array_list[i_1]

    return array_list


def multiply(array_list, i_1, i_2):
    array_list[i_1] = array_list[i_1] * array_list[i_2]

    return array_list


def decrease(array_list):
    for el in array:
        array_list[array_list.index(el)] -= 1

    return array_list
    pass


array = list(map(int, input().split()))
command = input()

while not command == "end":
    action = command.split()[0]

    if action == "swap":
        index_1 = int(command.split()[1])
        index_2 = int(command.split()[2])
        array = swap(array, index_1, index_2)
    elif action == "multiply":
        index_1 = int(command.split()[1])
        index_2 = int(command.split()[2])
        array = multiply(array, index_1, index_2)
    elif action == "decrease":
        array = decrease(array)

    command = input()

print(", ".join(map(str, array)))