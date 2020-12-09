import re

string = input().lower()
word = input().lower()

pattern = fr"\b{word}\b"

result = re.findall(pattern, string)
print(result.count(word))