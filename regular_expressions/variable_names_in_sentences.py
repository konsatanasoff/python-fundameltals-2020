import re

pattern = r"((?<=^_)|(?<=\s_))[A-Za-z0-9]+\b"


string = input()

valid_names = re.finditer(pattern, string)

result = [el.group() for el in re.finditer(pattern, string)]

print(','.join(result))
