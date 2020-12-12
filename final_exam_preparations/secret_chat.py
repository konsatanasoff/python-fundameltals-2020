def insert_space(string, i):
    left_side = string[:i]
    right_side = string[i:]
    new_message = left_side + " " + right_side
    print(new_message)
    return new_message


def reverse(string, substring):
    if substring not in string:
        print("error")

    else:
        new_str = string.replace(substring, '', 1)
        sub_reversed = substring[::-1]
        string = new_str + sub_reversed
        print(string)
    return string


def change_all(string, sub, to_replace):
    string = string.replace(sub, to_replace)
    print(string)
    return string


message = input()
command = input()

while not command == "Reveal":
    action = command.split(":|:")[0]

    if action == "InsertSpace":
        index = command.split(":|:")[1]
        index = int(index)
        message = insert_space(message, index)

    elif action == "Reverse":
        substring = command.split(":|:")[1]
        message = reverse(message, substring)
    elif action == "ChangeAll":
        substring, replacement = command.split(":|:")[1:]
        message = change_all(message, substring, replacement)

    command = input()

print(f"You have a new text message: {message}")