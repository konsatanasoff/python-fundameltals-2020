collection = input().split("|")
budget = float(input())

total_profit = 0
total_spent = []

for item in collection:
    item_type, price = item.split("->")
    price = float(price)

    if item_type == "Clothes" and price > 50:
        continue
    elif item_type == "Shoes" and price > 35:
        continue
    elif item_type == "Accessories" and price > 20.50:
        continue

    if budget >= price:
        budget -= price
        profit = price * 0.40
        total_profit += profit
        total_spent.append(price + profit)

for el in total_spent:
    print(f"{el:.2f}", end=' ')
print()
print(f"Profit: {total_profit:.2f}")

budget += sum(total_spent)

if budget >= 150:
    print(f"Hello, France!")
else:
    print(f"Time to go.")