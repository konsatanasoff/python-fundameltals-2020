import re


pattern = r"^>>(?P<item>[a-zA-Z]+)<{2}(?P<price>[0-9]+\.?[0-9]+)!(?P<quantity>\d+)"

items = []
total_price = 0

while True:
    try:
        line = input()
        data = re.finditer(pattern, line)
        for i in data:
            item = i.group(1)
            price = float(i.group(2))
            quantity = int(i.group(3))
            items.append(item)
            total_price += price * quantity
    except EOFError:
        break

print(f"Bought furniture:")
for item in items:
    print(item)
print(f"Total money spend: {total_price:.2f}" )