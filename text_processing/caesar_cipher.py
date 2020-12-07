line = input()

result = ""

for char in line:
    result += chr(ord(char) + 3)

print(result)