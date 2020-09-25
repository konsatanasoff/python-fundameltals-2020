budget = float(input())
flour_price = float(input())

eggs = flour_price * 0.75
milk = flour_price * 1.25 * 0.25
total_price = flour_price + eggs + milk
count = 0
money_left = budget
current_colored_eggs = 0

while money_left > total_price:
    money_left -= total_price
    count += 1
    current_colored_eggs += 3
    if count % 3 == 0:
        current_colored_eggs -= count - 2

print(f'You made {count} cozonacs! Now you have {current_colored_eggs} eggs and {money_left:.2f}BGN left.')