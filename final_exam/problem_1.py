def cut(string, i, l):
    new_string = string[i:i+l]
    print(new_string)


def find_index(string, char):
    indexes = []
    for i in range(len(string)):
        if string[i] == char:
            indexes.append(i)
    found_index = indexes[0]
    print(found_index)


def end(string_data, string):
    ends_with = False
    first_part = string_data[:len(string_data) - len(string)]
    new_string = first_part + string
    if string_data == new_string:
        ends_with = True
    print(ends_with)


data = input()

command = input()

while not command == "Done":
    action = command.split()[0]

    if action == "Change":
        char, replacement = command.split()[1:]
        data = data.replace(char, replacement)
        print(data)
    elif action == "Includes":
        included_string = command.split()[1]
        is_included = False
        if included_string in data:
            is_included = True
        print(is_included)

    elif action == "End":
        string = command.split()[1]
        end(data, string)
    elif action == "Uppercase":
        data = data.upper()
        print(data)
    elif action == "FindIndex":
        char = command.split()[1]
        find_index(data, char)
    elif action == "Cut":
        start_index, length = command.split()[1:]
        start_index = int(start_index)
        length = int(length)
        cut(data, start_index, length)

    command = input()