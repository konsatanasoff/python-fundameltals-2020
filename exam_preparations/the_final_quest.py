def delete(my_list, i):
    if i + 1 in range(len(my_list)):
        my_list.remove(my_list[i + 1])
    return my_list


def swap(my_list, w1, w2):
    if w1 in my_list and w2 in my_list:
        i_1 = my_list.index(w1)
        i_2 = my_list.index(w2)
        my_list[i_1], my_list[i_2] = my_list[i_2], my_list[i_1]
    return my_list


def put(my_list, w, i):
    if 0 <= i - 1 <= len(my_list):
        my_list.insert(i - 1, w)
    return my_list


def sort(my_list):
    my_list = sorted(my_list, reverse=True)
    return my_list


def replace(my_list, w1, w2):
    if w2 in my_list:
        my_list[my_list.index(w2)] = w1
    return my_list


collection = input().split()
command = input()

while not command == "Stop":
    action = command.split()[0]

    if action == "Delete":
        index = int(command.split()[1])
        collection = delete(collection, index)

    elif action == "Swap":
        word_1 = command.split()[1]
        word_2 = command.split()[2]
        collection = swap(collection, word_1, word_2)

    elif action == "Put":
        word = command.split()[1]
        index = int(command.split()[2])
        collection = put(collection, word, index)

    elif action == "Sort":
        collection = sort(collection)

    elif action == "Replace":
        word_1 = command.split()[1]
        word_2 = command.split()[2]
        collection = replace(collection, word_1, word_2)

    command = input()

print(" ".join(collection))
