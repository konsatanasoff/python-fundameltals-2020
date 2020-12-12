import re

pattern = r"(\=|/)[A-Z][A-Za-z]{2,}\1"

data = input()
destinations = [el.group() for el in re.finditer(pattern, data)]
result = [el[1:-1] for el in destinations]

travel_points = sum([len(el) for el in result])

print(f"Destinations: {', '.join(result)}")
print(f"Travel Points: {travel_points}")

