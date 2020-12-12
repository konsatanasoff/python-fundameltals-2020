def move(data, letters):
    to_move = data[:letters]
    remaining = data[letters:]
    new_data = remaining + to_move
    return new_data


def insert(data, i, v):
    left_side = data[:i]
    right_side = data[i:]
    new_data = left_side + v + right_side
    return new_data


def change_all(data, substring, replacement):
    data = data.replace(substring, replacement)
    return data


string = input()
command = input()

while not command == "Decode":
    action = command.split("|")[0]

    if action == "Move":
        n_letters = command.split("|")[1]
        n_letters = int(n_letters)
        string = move(string, n_letters)
    elif action == "Insert":
        index, value = command.split("|")[1:]
        index = int(index)
        string = insert(string, index, value)
    elif action == "ChangeAll":
        substring, replacement = command.split("|")[1:]
        string = change_all(string, substring, replacement)

    command = input()

print(f"The decrypted message is: {string}")