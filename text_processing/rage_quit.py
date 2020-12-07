line = input()

string = ""
result = ""
index = 0

while index < len(line):
    if not line[index].isdigit():
        string += line[index]
        index += 1
    else:
        num = ''
        while index < len(line) and line[index].isdigit():
            num += line[index]
            index += 1
        num = int(num)
        result += string.upper() * num
        string = ""

print(f"Unique symbols used: {len(set(result))}")
print(result)