import re


pattern = r"(#|\|)(?P<item>[A-Za-z\s]+)\1(?P<date>[0-9]{2}/[0-9]{2}/[0-9]{2})\1(?P<calories>[0-9][0-9]{0,3}|10000)\1"

string = input()

data = re.finditer(pattern, string)

items = []
total_calories = 0


for match in data:
    result = match.groupdict()
    items.append(result)
    total_calories += int(result["calories"])


days = total_calories // 2000
print(f"You have food to last you for: {days} days!")

for item in items:
    print(f"Item: {item['item']}, Best before: {item['date']}, Nutrition: {item['calories']}")
