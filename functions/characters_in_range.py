first_char = input()
last_char = input()


def char_range():
    char_list = []
    ascii_list = []

    for char in range(ord(first_char) + 1, ord(last_char)):
        char_list.append(char)

    for item in char_list:
        ascii_list.append(chr(item))

    result = ' ' .join(ascii_list)
    return result


print(char_range())