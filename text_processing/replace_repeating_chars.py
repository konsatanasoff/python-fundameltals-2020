line = input()

result = ""
current_letter = ""

for letter in line:
    if not letter == current_letter:
        result += letter
    current_letter = letter

print(result)