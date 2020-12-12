import re


def split(string):
    left_side = string[:len(string) // 2]
    right_side = string[len(string) // 2:]
    new_string = left_side + " " + right_side
    return new_string


pattern = r"(#|@)[a-zA-z]{3,}\1{2}[a-zA-Z]{3,}\1"

user_input = input()

word_data = [el.group() for el in re.finditer(pattern, user_input)]
split_word_data = [split(el) for el in word_data]
split_words = [el.replace("@", '').replace("#", '') for el in split_word_data]
valid_words = [el.replace(' ', " <=> ") for el in split_words]

mirror_words = [el.split(" <=> ") for el in valid_words]
mirror_words = [el for el in mirror_words if el[0] == el[1][::-1]]
result = []

for word in mirror_words:
    result.append(f"{word[0]} <=> {word[1]}")

if valid_words:
    print(f"{len(valid_words)} word pairs found!")
else:
    print("No word pairs found!")

if mirror_words:
    print("The mirror words are:")
    print(', '.join(result))
else:
    print("No mirror words!")