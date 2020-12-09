import re

pattern = r"\b[w]{3}\.[a-zA-Z0-9\-]+(\.[a-z]+)+\b"
links = []

data = input()

while data:
    [links.append(el.group()) for el in re.finditer(pattern, data)]
    data = input()

for link in links:
    print(link)