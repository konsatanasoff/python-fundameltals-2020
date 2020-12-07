data = input().split()
alphabet_dict = {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'g': 7, 'f': 6, 'i': 9, 'h': 8, 'k': 11, 'j': 10, 'm': 13,
                 'l': 12, 'o': 15, 'n': 14, 'q': 17, 'p': 16, 's': 19, 'r': 18, 'u': 21, 't': 20, 'w': 23, 'v': 22,
                 'y': 25, 'x': 24, 'z': 26}

result = 0

for el in data:
    first_letter = el[0]
    last_letter = el[-1]
    number = int(el[1:-1])

    if first_letter.isupper():
        number /= alphabet_dict[first_letter.lower()]
    elif first_letter.islower():
        number *= alphabet_dict[first_letter.lower()]

    if last_letter.isupper():
        number -= alphabet_dict[last_letter.lower()]
    elif last_letter.islower():
        number += alphabet_dict[last_letter.lower()]

    result += number

print(f"{result:.2f}")

