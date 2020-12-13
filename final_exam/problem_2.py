import re

pattern = r"([\w+]|.+)>\d{3}\|[a-z]{3}\|[A-Z]{3}\|[^<|>]+<\1$"

n = int(input())

for _ in range(n):
    data = input()
    valid_data = [el.group() for el in re.finditer(pattern, data)]
    to_remove = [i.group(1) for i in re.finditer(pattern, data)]

    if not valid_data:
        print("Try another password!")
    else:
        remove = len(to_remove[0]) + 1

        new_data = valid_data[0][remove:]
        new_data = new_data[:len(new_data)-remove]

        string_pass = ''
        for i in range(len(new_data)):
            if new_data[i] == "|":
                continue
            else:
                string_pass += new_data[i]
        print(f"Password: {string_pass}")