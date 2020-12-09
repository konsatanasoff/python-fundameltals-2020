import re

line = input()

pattern = r"(^|(?<=\s))[a-z0-9]+[\._-]?[a-z0-9]+@[a-z]+\-?[a-z]+(\.[a-z]+\-?[a-z]+)+"

emails = re.finditer(pattern, line)

for email in emails:
    print(email.group())