command = input()

total_price = 0
taxes = 0

while not (command == "special" or command == "regular"):
    part_price = float(command)

    if part_price > 0:
        total_price += part_price
    else:
        print(f"Invalid price!")

    command = input()

if total_price == 0:
    print(f"Invalid order!")
else:
    print(f"Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price:.2f}$")
    taxes += total_price * 0.2
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    if command == "special":
        print(f"Total price: {(total_price + taxes) * 0.90:.2f}$")
    else:
        print(f"Total price: {total_price + taxes:.2f}$")