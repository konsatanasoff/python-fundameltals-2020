sequence = input()

char_dict = {}

for char in sequence:
    if char not in char_dict:
        if char == ' ':
            continue
        char_dict[char] = 1
    else:
        char_dict[char] += 1

for char, occurrences in char_dict.items():
    print(f"{char} -> {occurrences}")